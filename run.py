import pandas as pd
import random

from model import Passenger
from batch import Batch
from serving import Serving
from stream import Stream


if __name__ == '__main__':
    batch = Batch()
    serving = Serving()
    stream = Stream()

    data = pd.read_csv('train.csv')
    columns = list(data.columns)

    attributes = ['PassengerId',
                  'Age', 'SibSp', 'Parch', 'Fare',
                  'Sex', 'Pclass', 'Embarked',
                  'Name', 'Ticket', 'Cabin']

    indices = [columns.index(_) for _ in attributes]

    counter = [0, 0]
    size = random.randint(1, 3)

    while counter[1] + size < data.shape[0]:
        selection = data.iloc[counter[1]:counter[1]+size, :].values.tolist()

        labels = [_[1] for _ in selection]
        passengers = [Passenger(*[_[idx] for idx in indices]) for _ in selection]

        # start of day
        if not serving.overall_counts:
            print 'not enough data points'
        else:
            for passenger in passengers:
                result = stream.respond(passenger)

                for feature_name in ['embarked', 'pclass', 'sex']:
                    result += serving.respond('feature', (feature_name, passenger.get(feature_name)))

                print counter[0], [round(_, 3) for _ in result]

        # end of day
        for i in xrange(size):
            batch.ingest(labels[i], passengers[i])
            batch.process()

            serving.ingest(batch.passengers, batch.feature_counts)
            serving.process()

        counter[0] += 1
        counter[1] += size
        size = random.randint(1, 3)

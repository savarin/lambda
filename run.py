import pandas as pd
import random
import time

from data import Passenger
from batch import Batch
from serving import Serving
from stream import Stream
from model import Model


if __name__ == '__main__':
    batch = Batch()
    serving = Serving()
    stream = Stream()
    model = Model()

    data = pd.read_csv('train.csv')
    columns = list(data.columns)

    attributes = ['PassengerId',
                  'Age', 'SibSp', 'Parch', 'Fare',
                  'Sex', 'Pclass', 'Embarked',
                  'Name', 'Ticket', 'Cabin']

    indices = [columns.index(_) for _ in attributes]

    counter = [0, 0]
    metrics = [0, 0]
    size = random.randint(1, 3)

    while counter[1] + size < data.shape[0]:
        selection = data.iloc[counter[1]:counter[1]+size, :].values.tolist()

        labels = [_[1] for _ in selection]
        passengers = [Passenger(*[_[idx] for idx in indices]) for _ in selection]

        # start of day
        if not serving.overall_counts:
            print 'no batch signals'
        else:
            for i in xrange(size):
                result = stream.respond(passengers[i])

                for feature_name in ['embarked', 'pclass', 'sex']:
                    key = (feature_name, passengers[i].get(feature_name))
                    result += serving.respond('feature', key)

                if model.classifier:
                    prediction = model.predict(result)[0]
                    metrics[0] += 1

                    if prediction == labels[i]:
                        metrics[1] += 1

                    print counter[0], prediction, labels[i]
                else:
                    print counter[0], 'no trained model'

        # end of day
        for i in xrange(size):
            batch.ingest(labels[i], passengers[i])
            batch.process()

            serving.ingest(batch.passengers, batch.feature_counts)
            serving.process()

            model.ingest(labels[i], passengers[i].get('idx'))

        if counter[0] and counter[0] % 7 == 0:
            print 'model performance: ', metrics[1] / float(metrics[0]) if metrics[0] else 0

            X_train = [serving.respond('passenger', _) for _ in model.indices]
            y_train = model.labels

            print 'model training in progress...'
            model.fit(X_train, y_train)

            time.sleep(0.2)

        counter[0] += 1
        counter[1] += size
        size = random.randint(1, 3)

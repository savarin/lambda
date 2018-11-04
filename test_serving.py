import pandas as pd
from model import Passenger
from batch import Batch
from serving import Serving


def test_serving_process():
    batch = Batch()
    serving = Serving()

    data = pd.read_csv('train.csv').head(10)
    columns = list(data.columns)

    attributes = ['PassengerId',
                  'Age', 'SibSp', 'Parch', 'Fare',
                  'Sex', 'Pclass', 'Embarked',
                  'Name', 'Ticket', 'Cabin']

    indices = [columns.index(_) for _ in attributes]

    for i, item in enumerate(data.values.tolist()):
        label = item[1]
        passenger = Passenger(*[item[_] for _ in indices])

        batch.ingest(label, passenger)

    batch.process()

    serving.ingest(batch.feature_counts)
    serving.process()

    assert serving.final_counts[('embarked', 'C')] == [2, 2, 1.]
    assert serving.final_counts[('embarked', 'S')] == [7, 3, 3/7.]
    assert serving.final_counts[('embarked', 'Q')] == [1, 0, 0.]

    assert serving.final_counts[('pclass', 1)] == [3, 2, 2/3.]
    assert serving.final_counts[('pclass', 2)] == [1, 1, 1.0]
    assert serving.final_counts[('pclass', 3)] == [6, 2, 1/3.]

    assert serving.final_counts[('sex', 'female')] == [5, 5, 1.]
    assert serving.final_counts[('sex', 'male')] == [5, 0, 0.]


if __name__ == '__main__':
    test_serving_process()

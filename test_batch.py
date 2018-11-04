import pandas as pd
from data import Passenger
from batch import Batch


def test_batch_process():
    batch = Batch()

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

    assert batch.feature_counts['embarked'][('C', 0)] == 0
    assert batch.feature_counts['embarked'][('S', 0)] == 4
    assert batch.feature_counts['embarked'][('Q', 0)] == 1
    assert batch.feature_counts['embarked'][('C', 1)] == 2
    assert batch.feature_counts['embarked'][('S', 1)] == 3
    assert batch.feature_counts['embarked'][('Q', 1)] == 0

    assert batch.feature_counts['pclass'][(1, 0)] == 1
    assert batch.feature_counts['pclass'][(2, 0)] == 0
    assert batch.feature_counts['pclass'][(3, 0)] == 4
    assert batch.feature_counts['pclass'][(1, 1)] == 2
    assert batch.feature_counts['pclass'][(2, 1)] == 1
    assert batch.feature_counts['pclass'][(3, 1)] == 2

    assert batch.feature_counts['sex'][('female', 0)] == 0
    assert batch.feature_counts['sex'][('male', 0)] == 5
    assert batch.feature_counts['sex'][('female', 1)] == 5
    assert batch.feature_counts['sex'][('male', 1)] == 0


if __name__ == '__main__':
    test_batch_process()

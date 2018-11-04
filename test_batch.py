import pandas as pd
from model import Passenger
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


# def test_convert_counts():
#     feature_counts = {
#         'Pclass': {
#             (1, 0): 1,
#             (2, 0): 0,
#             (3, 0): 4,
#             (1, 1): 2,
#             (2, 1): 1,
#             (3, 1): 2
#         }
#     }

#     final_counts = convert_counts(feature_counts)

#     assert final_counts[('Pclass', 1)] == [3, 2, 2/3.]
#     assert final_counts[('Pclass', 2)] == [1, 1, 1.]
#     assert final_counts[('Pclass', 3)] == [6, 2, 1/3.]


# def test_respond_counts():
#     final_counts = {
#         ('Pclass', 1): [3, 2, 2/3.],
#         ('Pclass', 2): [1, 1, 1.],
#         ('Pclass', 3): [6, 2, 1/3.],
#     }

#     assert respond_counts(final_counts, 'Pclass', 1, 'all') == 3
#     assert respond_counts(final_counts, 'Pclass', 1, 'ones') == 2
#     assert respond_counts(final_counts, 'Pclass', 1, 'ratio') == 2/3.
#     assert respond_counts(final_counts, 'Pclass', 2, 'all') == 1
#     assert respond_counts(final_counts, 'Pclass', 2, 'ones') == 1
#     assert respond_counts(final_counts, 'Pclass', 2, 'ratio') == 1.
#     assert respond_counts(final_counts, 'Pclass', 3, 'all') == 6
#     assert respond_counts(final_counts, 'Pclass', 3, 'ones') == 2
#     assert respond_counts(final_counts, 'Pclass', 3, 'ratio') == 1/3.
#     assert respond_counts(final_counts, None, None, None) == -1


# if __name__ == '__main__':
#     test_convert_counts()
#     test_respond_counts()

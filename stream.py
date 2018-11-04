import pandas as pd
import time
import random


class Signal(object):
    def __init__(self, columns, feature_names, categorical):
        self.columns = columns
        self.feature_names = feature_names
        self.categorical = categorical
        self.indices = [self.columns.index(_) for _ in feature_names]

        self.dictionary = {
            ('Sex', 'female'): [1, 0],
            ('Sex', 'male'): [0, 1],
            ('Pclass', 1): [1, 0, 0],
            ('Pclass', 2): [0, 1, 0],
            ('Pclass', 3): [0, 0, 1],
            ('Embarked', 'C'): [1, 0, 0],
            ('Embarked', 'S'): [0, 1, 0],
            ('Embarked', 'Q'): [0, 0, 1],
            ('Sex', None): [0, 0],
            ('Pclass', None): [0, 0, 0],
            ('Embarked', None): [0, 0, 0],
        }

    def convert(self, event):
        feature_values = [event[_] for _ in self.indices]
        result = []

        for i, item in enumerate(self.feature_names):
            if not self.categorical[i]:
                result.append(feature_values[i])
                continue

            key = (item, feature_values[i])

            if key in self.dictionary:
                result += self.dictionary[key]
            else:
                result += self.dictionary[(item, None)]

        return result


class Day(object):
    def __init__(self):
        self.limit = random.randint(1, 3)
        self.data = []

    def push(self, item):
        self.data.append(item)

    def is_full(self):
        return self.limit <= len(self.data)

    def refresh(self):
        self.limit = random.randint(1, 3)
        self.data = []


def run():
    data = pd.read_csv('train.csv').head(10)
    columns = list(data.columns)

    signal = Signal(columns,
                    ['Age', 'Sex', 'Pclass', 'Embarked'],
                    [False, True, True, True])
    day = Day()

    for i, item in enumerate(data.values.tolist()):
        day.push(item)
        print signal.convert(item)

        if day.is_full():
            print day.data
            day.refresh()

        time.sleep(0.1)


if __name__ == '__main__':
    run()

import pandas as pd
from collections import defaultdict
from functools import reduce


def collect_counts(feature_array, feature_values):
    result = {}

    for i, item in enumerate(feature_values):
        if not item:
            feature_values[i] = set([_[i] for _ in feature_array])

    for item0 in feature_values[0]:
        for item1 in feature_values[1]:
            counts = map(lambda x: int(x[0] == item0 and x[1] == item1), feature_array)
            counts = reduce(lambda x, y: x + y, counts)
            result[(item0, item1)] = counts

    return result


def run():
    data = pd.read_csv('train.csv')

    feature_array = data[['Pclass', 'Survived']].values.tolist()
    feature_values = [None, [0, 1]]

    print collect_counts(feature_array, feature_values)


if __name__ == '__main__':
    run()
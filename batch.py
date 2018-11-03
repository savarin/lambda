import pandas as pd
from collections import defaultdict
from functools import reduce


def run():
    data = pd.read_csv('train.csv')

    feature_names = ['Pclass', 'Survived']
    feature_values = [None, [0, 1]]

    feature_array = data[feature_names].values.tolist()
    feature_counter = {}

    for i, item in enumerate(feature_values):
        if not item:
            feature_values[i] = set([_[i] for _ in feature_array])

    for item0 in feature_values[0]:
        for item1 in feature_values[1]:
            result = map(lambda x: int(x[0] == item0 and x[1] == item1), feature_array)
            result = reduce(lambda x, y: x + y, result)
            feature_counter[(item0, item1)] = result

    print feature_counter


if __name__ == '__main__':
    run()
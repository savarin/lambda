import pandas as pd
from collections import defaultdict
from functools import reduce


def run_1():
    data = pd.read_csv('train.csv')

    feature_name = 'Pclass'
    feature_uniques = set()
    feature_array = data[feature_name].values.tolist()

    for i, item in enumerate(feature_array):
        if item not in feature_uniques:
            feature_uniques.add(item)
            result = map(lambda x: int(x == item), feature_array)
            result = reduce(lambda x, y: x + y, result)
            print item, result


def run_2():
    data = pd.read_csv('train.csv')

    feature_names = ['Pclass', 'Survived']
    feature_uniques = set()
    feature_array = data[feature_names].values.tolist()

    for i, item in enumerate(feature_array):
        if item[0] not in feature_uniques:
            feature_uniques.add(item[0])
            result = map(lambda x: int(x[0] == item[0] and x[1] == 1), feature_array)
            result = reduce(lambda x, y: x + y, result)
            print item[0], result


if __name__ == '__main__':
    run_1()
    run_2()
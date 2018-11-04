import pandas as pd
from functools import reduce
from model import Passenger


class Batch(object):
    def __init__(self):
        self.counter = 0
        self.labels = []
        self.passengers = []

        self.feature_names = ['sex', 'pclass', 'embarked']
        self.feature_counts = {}

    def process(self):
        for feature_name in self.feature_names:
            feature_array = []

            for i in xrange(self.counter):
                item = (self.labels[i], self.passengers[i].get(feature_name))
                feature_array.append(item)

            print feature_array

    def ingest(self, label, passenger):
        self.counter += 1
        self.labels.append(label)
        self.passengers.append(passenger)

        self.process()


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


def convert_counts(feature_counts):
    result = {}

    for feature_name, v1 in feature_counts.iteritems():
        for feature_value_pair, counts in v1.iteritems():
            key = (feature_name, feature_value_pair[0])

            if counts == 0:
                continue

            if key not in result:
                result[key] = [counts, 0, 0]
            else:
                result[key][0] += counts

            if feature_value_pair[1] == 1:
                result[key][1] = counts

    for key, v in result.iteritems():
        ratio = v[1] / float(v[0])
        result[key] = [v[0], v[1], ratio]

    return result


def respond_counts(final_counts, feature_name, feature_value, signal_type):
    if (feature_name, feature_value) in final_counts:
        result = final_counts[(feature_name, feature_value)]

        if signal_type == 'all':
            return result[0]
        elif signal_type == 'ones':
            return result[1]
        elif signal_type == 'ratio':
            return result[2]

    return -1


def run_():
    data = pd.read_csv('train.csv')
    feature_counts = {}

    for i, item in enumerate(['Pclass', 'Sex', 'Embarked']):
        feature_names = [item, 'Survived']
        feature_array = data[feature_names].values.tolist()
        feature_values = [None, [0, 1]]

        feature_counts[item] = collect_counts(feature_array, feature_values)

    final_counts = convert_counts(feature_counts)

    for i in xrange(1, 4):
        print i, respond_counts(final_counts, 'Pclass', i, 'ratio')

    for item in ['female', 'male']:
        print item, respond_counts(final_counts, 'Sex', item, 'ratio')

    for item in ['C', 'S', 'Q']:
        print item, respond_counts(final_counts, 'Embarked', item, 'ratio')


if __name__ == '__main__':
    run()

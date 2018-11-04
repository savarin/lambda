from functools import reduce


class Batch(object):
    def __init__(self):
        self.counter = 0
        self.labels = []
        self.passengers = []

        self.feature_names = ['sex', 'pclass', 'embarked']
        self.feature_counts = {}

    def ingest(self, label, passenger):
        self.counter += 1
        self.labels.append(label)
        self.passengers.append(passenger)

    def count(self, feature_array, feature_values):
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

    def process(self):
        for feature_name in self.feature_names:
            feature_array = []

            for i in xrange(self.counter):
                feature_array.append((self.passengers[i].get(feature_name), self.labels[i]))

            feature_values = [None, [0, 1]]
            self.feature_counts[feature_name] = self.count(feature_array, feature_values)


# def respond_counts(final_counts, feature_name, feature_value, signal_type):
#     if (feature_name, feature_value) in final_counts:
#         result = final_counts[(feature_name, feature_value)]

#         if signal_type == 'all':
#             return result[0]
#         elif signal_type == 'ones':
#             return result[1]
#         elif signal_type == 'ratio':
#             return result[2]

#     return -1

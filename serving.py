

class Serving(object):
    def __init__(self):
        self.passengers = []
        self.feature_counts = {}

        self.overall_counts = {}
        self.signals = {}

    def ingest(self, passengers, feature_counts):
        self.passengers = passengers
        self.feature_counts = feature_counts

    def convert(self, feature_counts):
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

    def process(self):
        self.overall_counts = self.convert(self.feature_counts)

        for passenger in self.passengers:
            result = passenger.featurize()

            for feature_name in ['embarked', 'pclass', 'sex']:
                key = (feature_name, passenger.get(feature_name))
                result += self.overall_counts.get(key, [-1, -1, -1])

            self.signals[passenger.get('idx')] = result

    def respond(self, id_type, id_key):
        if id_type == 'passenger':
            return self.signals.get(id_key, None)
        elif id_type == 'feature':
            return self.overall_counts.get(id_key, (-1, -1, -1))

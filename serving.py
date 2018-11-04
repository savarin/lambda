

class Serving(object):
    def __init__(self):
        self.feature_counts = {}
        self.final_counts = {}

    def ingest(self, feature_counts):
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
        self.final_counts = self.convert(self.feature_counts)

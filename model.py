from sklearn.ensemble import RandomForestClassifier


class Model(object):
    def __init__(self):
        self.counter = 0
        self.labels = []
        self.indices = []
        self.classifier = None

    def ingest(self, label, idx):
        self.counter += 1
        self.labels.append(label)
        self.indices.append(idx)

    def fit(self, signals, labels):
        self.classifier = RandomForestClassifier(n_estimators=100)
        self.classifier.fit(signals, labels)

    def predict(self, signals):
        return self.classifier.predict(signals)

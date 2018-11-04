

class Stream(object):
    def __init__(self):
        self.counter = 0

    def respond(self, passenger):
        return passenger.featurize()

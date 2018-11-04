import pandas as pd
import time
import random


class Day(object):
    def __init__(self):
        self.limit = random.randint(1, 3)
        self.data = []

    def refresh(self):
        self.limit = random.randint(1, 3)
        self.data = []

    def push(self, item):
        self.data.append(item)

    def is_full(self):
        return self.limit <= len(self.data)


def run():
    data = pd.read_csv('train.csv').head(10)
    columns = list(data.columns)

    day = Day()

    for i, item in enumerate(data.values.tolist()):
        day.push(item)

        if day.is_full():
            print day.data
            day.refresh()

        time.sleep(0.1)


if __name__ == '__main__':
    run()

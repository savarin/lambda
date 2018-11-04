import numpy as np


class Passenger(object):
    def __init__(self, idx,
                 age, sibsp, parch, fare,
                 sex, pclass, embarked,
                 name, ticket, cabin):
        self.idx = idx
        self.age = age
        self.sibsp = sibsp
        self.parch = parch
        self.fare = fare
        self.sex = sex
        self.pclass = pclass
        self.embarked = embarked
        self.name = name
        self.ticket = ticket
        self.cabin = cabin


class Signal(object):
    def __init__(self):
        self.values = []
        self.definition = [
            ('age', lambda x: x.age if not np.isnan(x.age) else -1),
            ('sibsp', lambda x: x.sibsp if not np.isnan(x.sibsp) else -1),
            ('parch', lambda x: x.parch if not np.isnan(x.parch) else -1),
            ('fare', lambda x: x.fare if not np.isnan(x.fare) else -1),
            ('sex_female', lambda x: int(x.sex == 'female')),
            ('sex_male', lambda x: int(x.sex == 'male')),
            ('pclass_1', lambda x: int(x.pclass == 1)),
            ('pclass_2', lambda x: int(x.pclass == 2)),
            ('pclass_3', lambda x: int(x.pclass == 3)),
            ('embarked_C', lambda x: int(x.embarked == 'C')),
            ('embarked_S', lambda x: int(x.embarked == 'S')),
            ('embarked_Q', lambda x: int(x.embarked == 'Q')),
        ]

    def ingest(self, passenger):
        for _, action in self.definition:
            self.values.append(action(passenger))


if __name__ == '__main__':
    passenger = Passenger(0, 21, 0, 0, 100, 'female', 1, 'C', '', '', '')

    signal = Signal()
    signal.ingest(passenger)

    print signal.values

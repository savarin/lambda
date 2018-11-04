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

    def get(self, attribute):
        return eval('self.' + attribute)

    def featurize(self):
        definition = [
            ('age', self.age if not np.isnan(self.age) else -1),
            ('sibsp', self.sibsp if not np.isnan(self.sibsp) else -1),
            ('parch', self.parch if not np.isnan(self.parch) else -1),
            ('fare', self.fare if not np.isnan(self.fare) else -1),
            ('sex_female', int(self.sex == 'female')),
            ('sex_male', int(self.sex == 'male')),
            ('pclass_1', int(self.pclass == 1)),
            ('pclass_2', int(self.pclass == 2)),
            ('pclass_3', int(self.pclass == 3)),
            ('embarked_C', int(self.embarked == 'C')),
            ('embarked_S', int(self.embarked == 'S')),
            ('embarked_Q', int(self.embarked == 'Q')),
        ]

        return [_[1] for _ in definition]

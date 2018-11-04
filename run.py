import pandas as pd
import random

from model import Passenger


if __name__ == '__main__':
    data = pd.read_csv('train.csv').head(10)
    columns = list(data.columns)

    attributes = ['PassengerId',
                  'Age', 'SibSp', 'Parch', 'Fare',
                  'Sex', 'Pclass', 'Embarked',
                  'Name', 'Ticket', 'Cabin']

    indices = [columns.index(_) for _ in attributes]

    counter = 0
    size = random.randint(1, 3)

    while counter + size < data.shape[0]:
        daily_data = data.iloc[counter:counter+size, :].values.tolist()

        daily_data = [(_[1], [_[idx] for idx in indices]) for _ in daily_data]
        daily_data = [(_[0], Passenger(*_[1])) for _ in daily_data]
        print daily_data

        counter += size
        size = random.randint(1, 3)

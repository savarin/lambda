from model import Passenger


def test_passenger_initialize():
    passenger = Passenger(0, 21, 0, 0, 100, 'female', 1, 'C', '', '', '')
    
    assert passenger.featurize() == [21, 0, 0, 100, 1, 0, 1, 0, 0, 1, 0, 0]

    assert passenger.get('age') == 21
    assert passenger.get('sex') == 'female'
    assert passenger.get('pclass') == 1


if __name__ == '__main__':
    test_passenger_initialize()
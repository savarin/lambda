from batch import collect_counts


def test_collect_counts():
    feature_array = [[3, 0], [1, 1],
                     [3, 1], [1, 1],
                     [3, 0], [3, 0],
                     [1, 0], [3, 0],
                     [3, 1], [2, 1]]
    feature_values = [None, [0, 1]]

    result = collect_counts(feature_array, feature_values)

    assert result[(1, 0)] == 1
    assert result[(2, 0)] == 0
    assert result[(3, 0)] == 4
    assert result[(1, 1)] == 2
    assert result[(2, 1)] == 1
    assert result[(3, 1)] == 2

def test_convert_counts():
    feature_counts = {
        'Pclass': {
            (1, 0): 1,
            (2, 0): 0,
            (3, 0): 4,
            (1, 0): 2,
            (2, 0): 1,
            (3, 0): 2
        }
    }

    result = convert_counts(feature_counts)

    assert result[('Pclass', 1)] == [3, 2, 2/3.]
    assert result[('Pclass', 2)] == [1, 1, 1.]
    assert result[('Pclass', 3)] == [6, 2, 1/3.]

if __name__ == '__main__':
    test_collect_counts()
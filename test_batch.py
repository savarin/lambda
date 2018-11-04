from batch import collect_counts, convert_counts, respond_counts


def test_collect_counts():
    feature_array = [[3, 0], [1, 1],
                     [3, 1], [1, 1],
                     [3, 0], [3, 0],
                     [1, 0], [3, 0],
                     [3, 1], [2, 1]]
    feature_values = [None, [0, 1]]

    feature_counts = collect_counts(feature_array, feature_values)

    assert feature_counts[(1, 0)] == 1
    assert feature_counts[(2, 0)] == 0
    assert feature_counts[(3, 0)] == 4
    assert feature_counts[(1, 1)] == 2
    assert feature_counts[(2, 1)] == 1
    assert feature_counts[(3, 1)] == 2


def test_convert_counts():
    feature_counts = {
        'Pclass': {
            (1, 0): 1,
            (2, 0): 0,
            (3, 0): 4,
            (1, 1): 2,
            (2, 1): 1,
            (3, 1): 2
        }
    }

    final_counts = convert_counts(feature_counts)

    assert final_counts[('Pclass', 1)] == [3, 2, 2/3.]
    assert final_counts[('Pclass', 2)] == [1, 1, 1.]
    assert final_counts[('Pclass', 3)] == [6, 2, 1/3.]


def test_respond_counts():
    final_counts = {
        ('Pclass', 1): [3, 2, 2/3.],
        ('Pclass', 2): [1, 1, 1.],
        ('Pclass', 3): [6, 2, 1/3.],
    }

    assert respond_counts(final_counts, 'Pclass', 1, 'all') == 3
    assert respond_counts(final_counts, 'Pclass', 1, 'ones') == 2
    assert respond_counts(final_counts, 'Pclass', 1, 'ratio') == 2/3.
    assert respond_counts(final_counts, 'Pclass', 2, 'all') == 1
    assert respond_counts(final_counts, 'Pclass', 2, 'ones') == 1
    assert respond_counts(final_counts, 'Pclass', 2, 'ratio') == 1.
    assert respond_counts(final_counts, 'Pclass', 3, 'all') == 6
    assert respond_counts(final_counts, 'Pclass', 3, 'ones') == 2
    assert respond_counts(final_counts, 'Pclass', 3, 'ratio') == 1/3.
    assert respond_counts(final_counts, None, None, None) == -1


if __name__ == '__main__':
    test_collect_counts()
    test_convert_counts()
    test_respond_counts()

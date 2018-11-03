from batch import collect_counts


def test_collect_counts():
    feature_array = [[3, 0], [1, 1], [3, 1], [1, 1], [3, 0], [3, 0], [1, 0], [3, 0], [3, 1], [2, 1]]
    feature_values = [None, [0, 1]]

    result = collect_counts(feature_array, feature_values)

    assert result[(1, 0)] == 1
    assert result[(2, 0)] == 0
    assert result[(3, 0)] == 4
    assert result[(1, 1)] == 2
    assert result[(2, 1)] == 1
    assert result[(3, 1)] == 2


if __name__ == '__main__':
    test_collect_counts()
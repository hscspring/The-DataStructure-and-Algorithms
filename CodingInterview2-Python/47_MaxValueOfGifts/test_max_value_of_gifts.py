from max_value_of_gifts import get_max_value1, get_max_value2


def test33():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]
    assert get_max_value1(matrix) == 29
    assert get_max_value2(matrix) == 29


def test44():
    matrix = [
        [1, 10, 3, 8],
        [12, 2, 9, 6],
        [5, 7, 4, 11],
        [3, 7, 16, 5]]
    assert get_max_value1(matrix) == 53
    assert get_max_value2(matrix) == 53


def test14():
    matrix = [[1, 10, 3, 8]]
    assert get_max_value1(matrix) == 22
    assert get_max_value2(matrix) == 22


def test41():
    matrix = [[1], [12], [5], [3]]
    assert get_max_value1(matrix) == 21
    assert get_max_value2(matrix) == 21


def test11():
    matrix = [[3]]
    assert get_max_value1(matrix) == 3
    assert get_max_value2(matrix) == 3


def testnone1():
    matrix = [[]]
    assert get_max_value1(matrix) == 0
    assert get_max_value2(matrix) == 0


def testnone2():
    matrix = []
    assert get_max_value1(matrix) == 0
    assert get_max_value2(matrix) == 0

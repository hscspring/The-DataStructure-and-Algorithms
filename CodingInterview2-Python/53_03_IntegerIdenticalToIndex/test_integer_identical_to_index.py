from integer_identical_to_index import get_number_same_as_index


def test1():
    numbers = [-3, -1, 1, 3, 5]
    expected = 3
    assert get_number_same_as_index(numbers) == expected


def test2():
    numbers = [0, 1, 3, 5, 6]
    expected = 0
    assert get_number_same_as_index(numbers) == expected


def test3():
    numbers = [-1, 0, 1, 2, 4]
    expected = 4
    assert get_number_same_as_index(numbers) == expected


def test4():
    numbers = [-1, 0, 1, 2, 5]
    expected = -1
    assert get_number_same_as_index(numbers) == expected


def test5():
    numbers = [0]
    expected = 0
    assert get_number_same_as_index(numbers) == expected


def test6():
    numbers = [10]
    expected = -1
    assert get_number_same_as_index(numbers) == expected


def test7():
    assert get_number_same_as_index([]) == -1

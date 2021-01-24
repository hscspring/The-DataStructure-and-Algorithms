from continuous_squence_with_sum import find_continuous_sequence
from continuous_squence_with_sum import find_continuous_sequence2


def test1():
    res = find_continuous_sequence(1)
    assert res == []
    res2 = find_continuous_sequence2(1)
    assert res2 == []


def test2():
    res = find_continuous_sequence(3)
    assert res == [[1, 2]]
    res2 = find_continuous_sequence2(3)
    assert res2 == [[1, 2]]


def test3():
    res = find_continuous_sequence(4)
    assert res == []
    res2 = find_continuous_sequence2(4)
    assert res2 == []


def test4():
    res = find_continuous_sequence(9)
    assert res == [[2, 3, 4], [4, 5]]
    res2 = find_continuous_sequence2(9)
    assert res2 == [[2, 3, 4], [4, 5]]


def test5():
    res = find_continuous_sequence(15)
    assert res == [[1, 2, 3, 4, 5], [4, 5, 6], [7, 8]]
    res2 = find_continuous_sequence2(15)
    assert res2 == [[1, 2, 3, 4, 5], [4, 5, 6], [7, 8]]


def test6():
    res = find_continuous_sequence(100)
    assert res == [[9, 10, 11, 12, 13, 14, 15, 16], [18, 19, 20, 21, 22]]
    res2 = find_continuous_sequence2(100)
    assert res2 == [[9, 10, 11, 12, 13, 14, 15, 16], [18, 19, 20, 21, 22]]

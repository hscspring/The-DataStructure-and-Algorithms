from maximal_profit import get_max_diff


def test1():
    data = [4, 1, 3, 2, 5]
    assert get_max_diff(data) == 4


# 价格递增


def test2():
    data = [1, 2, 4, 7, 11, 16]
    assert get_max_diff(data) == 15


# 价格递减


def test3():
    data = [16, 11, 7, 4, 2, 1]
    assert get_max_diff(data) == -1


# 价格全部相同


def test4():
    data = [16, 16, 16, 16, 16]
    assert get_max_diff(data) == 0


def test5():
    data = [9, 11, 5, 7, 16, 1, 4, 2]
    assert get_max_diff(data) == 11


def test6():
    data = [2, 4]
    assert get_max_diff(data) == 2


def test7():
    data = [4, 2]
    assert get_max_diff(data) == -2

from add_two_numbers import add, add2


def test1():
    assert add(1, 2) == 3
    assert add2(1, 2) == 3


def test2():
    assert add(111, 899) == 1010
    assert add2(111, 899) == 1010


def test3():
    assert add(-1, 2) == 1
    # assert add2(-1, 2) == 1


def test4():
    assert add(1, -2) == -1
    # assert add2(1, -2) == -1


def test5():
    assert add(3, 0) == 3
    assert add2(3, 0) == 3


def test6():
    assert add(0, -4) == -4
    # assert add2(0, -4) == -4


def test7():
    assert add(-2, -8) == -10
    # assert add2(-2, -8) == -10

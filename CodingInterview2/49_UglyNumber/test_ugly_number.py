from ugly_number import get_ugly


def test1():
    assert get_ugly(0) == 0


def test1():
    assert get_ugly(1) == 1


def test2():
    assert get_ugly(2) == 2


def test3():
    assert get_ugly(3) == 3


def test4():
    assert get_ugly(4) == 4


def test5():
    assert get_ugly(5) == 5


def test6():
    assert get_ugly(6) == 6


def test7():
    assert get_ugly(7) == 8


def test8():
    assert get_ugly(8) == 9


def test9():
    assert get_ugly(9) == 10


def test10():
    assert get_ugly(10) == 12


def test11():
    assert get_ugly(11) == 15


def test1500():
    assert get_ugly(1500) == 859963392

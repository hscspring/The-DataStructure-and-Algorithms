from digits_in_sequence import digit_at_index


def test1():
    res = digit_at_index(5)
    assert res == 6


def test2():
    res = digit_at_index(13)
    assert res == 1


def test3():
    res = digit_at_index(19)
    assert res == 4


def test4():
    res = digit_at_index(10)
    assert res == 1


def test5():
    res = digit_at_index(189)
    assert res == 9


def test6():
    res = digit_at_index(190)
    assert res == 1


def test7():
    res = digit_at_index(1000)
    assert res == 3


def test8():
    res = digit_at_index(1001)
    assert res == 7


def test9():
    res = digit_at_index(1002)
    assert res == 0


def test10():
    assert digit_at_index(0) == 1


def test11():
    assert digit_at_index(-1) == -1


def test12():
    assert digit_at_index(-10) == -1

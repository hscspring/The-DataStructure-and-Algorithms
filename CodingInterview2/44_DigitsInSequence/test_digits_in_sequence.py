from digits_in_sequence import digit_at_index, digit_at_index2


def test1():
    assert digit_at_index(5) == 5
    assert digit_at_index2(5) == 5


def test2():
    assert digit_at_index(13) == 1
    assert digit_at_index2(13) == 1


def test3():
    assert digit_at_index(19) == 4
    assert digit_at_index2(19) == 4


def test4():
    assert digit_at_index(10) == 1
    assert digit_at_index(10) == 1


def test5():
    assert digit_at_index(189) == 9
    assert digit_at_index(189) == 9


def test6():
    assert digit_at_index(190) == 1
    assert digit_at_index(190) == 1


def test7():
    assert digit_at_index(1000) == 3
    assert digit_at_index(1000) == 3


def test8():
    assert digit_at_index(1001) == 7
    assert digit_at_index(1001) == 7


def test9():
    assert digit_at_index(1002) == 0
    assert digit_at_index(1002) == 0


def test10():
    assert digit_at_index(0) == 0
    assert digit_at_index2(0) == 0


def test11():
    assert digit_at_index(-1) == -1
    assert digit_at_index2(-1) == -1


def test12():
    assert digit_at_index(-10) == -1
    assert digit_at_index2(-10) == -1

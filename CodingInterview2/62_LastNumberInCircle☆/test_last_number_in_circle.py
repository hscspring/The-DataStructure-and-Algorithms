from last_number_in_circle import last_remaining, last_remaining2


def test1():
    assert last_remaining(5, 3) == 3
    assert last_remaining2(5, 3) == 3


def test2():
    assert last_remaining(5, 2) == 2
    assert last_remaining2(5, 2) == 2


def test3():
    assert last_remaining(6, 7) == 4
    assert last_remaining2(6, 7) == 4


def test4():
    assert last_remaining(6, 6) == 3
    assert last_remaining2(6, 6) == 3


def test5():
    assert last_remaining(0, 0) == -1
    assert last_remaining2(0, 0) == -1


def test6():
    assert last_remaining(4000, 997) == 1027
    assert last_remaining2(4000, 997) == 1027

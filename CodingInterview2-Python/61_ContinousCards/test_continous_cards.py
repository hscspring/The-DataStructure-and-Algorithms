from continous_cards import is_continous


def test1():
    data = [1, 3, 2, 5, 4]
    assert is_continous(data) == True


def test2():
    data = [1, 3, 2, 6, 4]
    assert is_continous(data) == False


def test3():
    data = [0, 3, 2, 6, 4]
    assert is_continous(data) == True


def test4():
    data = [0, 3, 1, 6, 4]
    assert is_continous(data) == False


def test5():
    data = [1, 3, 0, 5, 0]
    assert is_continous(data) == True


def test6():
    data = [1, 3, 0, 7, 0]
    assert is_continous(data) == False


def test7():
    data = [1, 0, 0, 5, 0]
    assert is_continous(data) == True


def test8():
    data = [1, 0, 0, 7, 0]
    assert is_continous(data) == False


def test9():
    data = [3, 0, 0, 0, 0]
    assert is_continous(data) == True


def test10():
    data = [0, 0, 0, 0, 0]
    assert is_continous(data) == True

# 有对子


def test11():
    data = [1, 0, 0, 1, 0]
    assert is_continous(data) == False


def test12():
    assert is_continous([]) == False

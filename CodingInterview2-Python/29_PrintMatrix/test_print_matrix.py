from print_matrix import print_matrix_clockwisely, make_matrix


def test11():
    m = make_matrix(1, 1)
    assert print_matrix_clockwisely(m) == [1]


def test22():
    m = make_matrix(2, 2)
    assert print_matrix_clockwisely(m) == [1, 2, 4, 3]


def test44():
    m = make_matrix(4, 4)
    assert print_matrix_clockwisely(m) == [
        1, 2, 3, 4,
        8, 12, 16, 15,
        14, 13, 9, 5,
        6, 7, 11, 10]


def test55():
    m = make_matrix(5, 5)
    assert print_matrix_clockwisely(m) == [
        1, 2, 3, 4, 5,
        10, 15, 20, 25, 24,
        23, 22, 21, 16, 11,
        6, 7, 8, 9, 14,
        19, 18, 17, 12, 13
    ]


def test51():
    m = make_matrix(5, 1)
    assert print_matrix_clockwisely(m) == [1, 2, 3, 4, 5]


def test52():
    m = make_matrix(5, 2)
    assert print_matrix_clockwisely(m) == [
        1, 2, 4, 6, 8, 10, 9, 7, 5, 3
    ]


def test53():
    m = make_matrix(5, 3)
    assert print_matrix_clockwisely(m) == [
        1, 2, 3, 6, 9, 12, 15, 14, 13, 10, 7, 4, 5, 8, 11
    ]


def test54():
    m = make_matrix(5, 4)
    assert print_matrix_clockwisely(m) == [
        1, 2, 3, 4,
        8, 12, 16, 20,
        19, 18, 17, 13, 9, 5,
        6, 7, 11, 15, 14, 10
    ]


def test15():
    m = make_matrix(1, 5)
    assert print_matrix_clockwisely(m) == [1, 2, 3, 4, 5]


def test25():
    m = make_matrix(2, 5)
    assert print_matrix_clockwisely(m) == [
        1, 2, 3, 4, 5, 10, 9, 8, 7, 6
    ]


def test35():
    m = make_matrix(3, 5)
    assert print_matrix_clockwisely(m) == [
        1, 2, 3, 4, 5, 10, 15, 14, 13, 12, 11, 6, 7, 8, 9
    ]


def test45():
    m = make_matrix(4, 5)
    assert print_matrix_clockwisely(m) == [
        1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6,
        7, 8, 9, 14, 13, 12
    ]


def test01():
    m = make_matrix(0, 1)
    assert print_matrix_clockwisely(m) == []


def test10():
    m = make_matrix(1, 0)
    assert print_matrix_clockwisely(m) == []


def test00():
    m = make_matrix(0, 0)
    assert print_matrix_clockwisely(m) == []

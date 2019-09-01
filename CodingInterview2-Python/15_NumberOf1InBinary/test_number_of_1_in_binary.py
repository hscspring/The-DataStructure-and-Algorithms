from number_of_1_in_binary import num_of1_right, num_of1_left, num_of1


def test_n0():
    assert num_of1(0) == 0
    assert num_of1_left(0) == 0
    assert num_of1_right(0) == 0

def test_n1():
    assert num_of1(1) == 1
    assert num_of1_left(1) == 1
    assert num_of1_right(1) == 1

def test_nm1():
    assert num_of1(-1) == 2
    assert num_of1_left(-1) == 2
    assert num_of1_right(-1) == 2

def test_n10():
    assert num_of1(10) == 2
    assert num_of1_left(10) == 2
    assert num_of1_right(10) == 2

def test_big():
    assert num_of1(0x7FFFFFFF) == 31
    assert num_of1_left(0x7FFFFFFF) == 31
    assert num_of1_right(0x7FFFFFFF) == 31

def test_bigm():
    assert num_of1(0xFFFFFFFF) == 32
    assert num_of1_left(0xFFFFFFFF) == 32
    assert num_of1_right(0xFFFFFFFF) == 32

def test_bigm2():
    assert num_of1(0x80000000) == 1
    assert num_of1_left(0x80000000) == 1
    assert num_of1_right(0x80000000) == 1
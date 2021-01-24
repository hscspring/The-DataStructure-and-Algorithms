from accumulate import sum1



def test0():
    assert sum1(0) == 0

def test1():
    assert sum1(1) == 1

def test5():
    assert sum1(5) == 15

def test10():
    assert sum1(10) == 55
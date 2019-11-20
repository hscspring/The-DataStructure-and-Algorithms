from find_once_number import find


def test1():
    lst = [1,1,2,2,3,4,4,5,5,6,6]
    assert (find(lst)) == 3

def test2():
    lst = [1,1,2,2,3,4,4,5,5]
    assert (find(lst)) == 3


def test3():
    lst = [1,1,2,3,3]
    assert (find(lst)) == 2


def test4():
    lst = [1,2,2,3,3,4,4,5,5,6,6]
    assert (find(lst)) == 1


def test5():
    lst = [1,1,2,2,3]
    assert (find(lst)) == 3

def test6():
    lst = [1,2,2,3,3]
    assert(find(lst)) == 1

def test7():
    lst = [2,2,3,4,4]
    assert(find(lst)) == 3

def test9():
    lst = [0,0,1,2,2]
    assert(find(lst)) == 1

def test9():
    lst = [4,4,5,5,6,7,7,8,8]
    assert (find(lst)) == 6

def test10():
    lst = [2,2]
    assert(find(lst)) == -1


def test11():
    lst = [2,3]
    assert(find(lst)) == 2
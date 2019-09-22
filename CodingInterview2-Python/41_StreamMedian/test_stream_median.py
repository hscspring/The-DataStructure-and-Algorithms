from stream_median import get_median


def test_odd():
    lst = [1,3,5,2,4,6,7]
    assert get_median(lst) == 4

def test_even():
    lst = [1,3,2,4]
    assert get_median(lst) == 2.5

def test_one():
    lst = [3]
    assert get_median(lst) == 3

def test_none():
    lst = []
    assert get_median(lst) == None

def test_loop():
    medians = []
    lst = [5,2,3,4,1,6,7,0,8]
    for i in range(len(lst)):
        median = get_median(lst)
        medians.append(median)
        lst.pop()
    assert medians == [4,3.5,4,3.5,3,3.5,3,3.5,5]
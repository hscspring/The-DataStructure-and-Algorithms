from numbers_appear_once import find_num_appear_once



def test_normal():
    data = [ 2, 4, 3, 6, 3, 2, 5, 5 ]
    assert find_num_appear_once(data) ==  [4, 6]

def test_no_repeat():
    data = [ 4, 6 ]
    assert find_num_appear_once(data) ==  [4, 6]

def test_multi_repeat():
    data = [ 4, 6, 1, 1, 1, 1 ]
    assert find_num_appear_once(data) ==  [4, 6]

def test_only_repeat():
    data = [1, 1, 2, 2]
    assert find_num_appear_once(data) == []

def test_none():
    data = []
    assert find_num_appear_once(data) == []
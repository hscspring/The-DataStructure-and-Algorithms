from more_than_half_number import more_than_half_num
from more_than_half_number import more_than_half_num_with_dict
from more_than_half_number import more_than_half_num_recurision

def test_exist():
    lst = [1, 2, 3, 2, 2, 2, 5, 4, 2]
    assert more_than_half_num(lst) == 2
    assert more_than_half_num_with_dict(lst) == 2
    assert more_than_half_num_recurision(lst) == 2

def test_notexist():
    lst = [1, 2, 3, 2, 4, 2, 5, 2, 3]
    assert more_than_half_num(lst) == 0
    assert more_than_half_num_with_dict(lst) == 0
    assert more_than_half_num_recurision(lst) == 0

def test_head():
    lst = [2, 2, 2, 2, 2, 1, 3, 4, 5]
    assert more_than_half_num(lst) == 2
    assert more_than_half_num_with_dict(lst) == 2
    assert more_than_half_num_recurision(lst) == 2

def test_tail():
    lst = [1, 3, 4, 5, 2, 2, 2, 2, 2]
    assert more_than_half_num(lst) == 2
    assert more_than_half_num_with_dict(lst) == 2
    assert more_than_half_num_recurision(lst) == 2

def test_one():
    lst = [1]
    assert more_than_half_num(lst) == 1
    assert more_than_half_num_with_dict(lst) == 1
    assert more_than_half_num_recurision(lst) == 1

def test_none():
    lst = []
    assert more_than_half_num(lst) == None
    assert more_than_half_num_with_dict(lst) == None
    assert more_than_half_num_recurision(lst) == None

def test_repeat():
    lst = [1, 1, 1, 1, 2, 2, 2, 2, 2]
    assert more_than_half_num(lst) == 2
    assert more_than_half_num_with_dict(lst) == 2
    assert more_than_half_num_recurision(lst) == 2
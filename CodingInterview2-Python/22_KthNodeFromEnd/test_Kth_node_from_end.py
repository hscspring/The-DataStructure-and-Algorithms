from Kth_node_from_end import find_kth_from_tail
from Kth_node_from_end import list2link

def test_normal():
    lst = [1,2,3,4,5]
    link = list2link(lst)
    assert find_kth_from_tail(link, 3).val == 3

def test_tail():
    lst = [1,2,3,4,5]
    link = list2link(lst)
    assert find_kth_from_tail(link, 1).val == 5

def test_head():
    lst = [1,2,3,4,5]
    link = list2link(lst)
    assert find_kth_from_tail(link, 5).val == 1

def test_none():
    lst = []
    link = list2link(lst)
    assert find_kth_from_tail(link, 1).val == None

def test_kbiger_than_len():
    lst = [1,2,3,4,5]
    link = list2link(lst)
    assert find_kth_from_tail(link, 6).val == None

def test_k0():
    lst = [1,2,3,4,5]
    link = list2link(lst)
    assert find_kth_from_tail(link, 0).val == None
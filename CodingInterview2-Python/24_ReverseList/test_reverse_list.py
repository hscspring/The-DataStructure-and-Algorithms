from reverse_list import reverse, reverse2, reverse3
from reverse_list import list2link, link2list

def test_one_node():
    lst = [1]
    link = list2link(lst)
    res = reverse(link)
    assert res.val == 1
    assert link2list(res) == [1]
    
    res = reverse2(list2link(lst))
    assert res.val == 1
    assert link2list(res) == [1]
    
    res = reverse3(list2link(lst))
    assert res.val == 1
    assert link2list(res) == [1]

def test_multiple_nodes():
    lst = [1,2,3,4,5]
    link = list2link(lst)
    
    res = reverse(link)
    assert res.val == 5
    assert link2list(res) == [5,4,3,2,1]
    
    res = reverse2(list2link(lst))
    assert res.val == 5
    assert link2list(res) == [5,4,3,2,1]
    
    res = reverse3(list2link(lst))
    assert res.val == 5
    assert link2list(res) == [5,4,3,2,1]

def test_none():
    lst = []
    link = list2link(lst)
    res = reverse(link)
    assert res == None
    res = reverse2(link)
    assert res == None
    res = reverse3(link)
    assert res == None
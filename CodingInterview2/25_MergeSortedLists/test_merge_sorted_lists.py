from merge_sorted_lists import merge, merge_recurision, merge2
from merge_sorted_lists import list2link, link2list


def test_no_repeat():
    lst1 = [1, 3, 5]
    lst2 = [2, 4, 6]
    link1 = list2link(lst1)
    link2 = list2link(lst2)
    link = merge_recurision(link1, link2)
    assert link2list(link) == [1, 2, 3, 4, 5, 6]
    link1 = list2link(lst1)
    link2 = list2link(lst2)
    link = merge(link1, link2)
    assert link2list(link) == [1, 2, 3, 4, 5, 6]
    link1 = list2link(lst1)
    link2 = list2link(lst2)
    link = merge2(link1, link2)
    assert link2list(link) == [1, 2, 3, 4, 5, 6]


def test_repeat():
    lst1 = [1, 3, 5]
    lst2 = [1, 3, 5]
    link1 = list2link(lst1)
    link2 = list2link(lst2)
    link = merge_recurision(link1, link2)
    assert link2list(link) == [1, 1, 3, 3, 5, 5]
    link1 = list2link(lst1)
    link2 = list2link(lst2)
    link = merge(link1, link2)
    assert link2list(link) == [1, 1, 3, 3, 5, 5]
    link1 = list2link(lst1)
    link2 = list2link(lst2)
    link = merge2(link1, link2)
    assert link2list(link) == [1, 1, 3, 3, 5, 5]


def test_unbanlance():
    lst1 = [1, 3, 5, 7, 9]
    lst2 = [2, 4]
    link1 = list2link(lst1)
    link2 = list2link(lst2)
    link = merge_recurision(link1, link2)
    assert link2list(link) == [1, 2, 3, 4, 5, 7, 9]
    link1 = list2link(lst1)
    link2 = list2link(lst2)
    link = merge(link1, link2)
    assert link2list(link) == [1, 2, 3, 4, 5, 7, 9]
    link1 = list2link(lst1)
    link2 = list2link(lst2)
    link = merge2(link1, link2)
    assert link2list(link) == [1, 2, 3, 4, 5, 7, 9]



def test_one_none():
    lst1 = [1, 3, 5]
    lst2 = []
    link1 = list2link(lst1)
    link2 = list2link(lst2)
    link = merge_recurision(link1, link2)
    assert link2list(link) == [1, 3, 5]
    link = merge(link1, link2)
    assert link2list(link) == [1, 3, 5]
    link = merge2(link1, link2)
    assert link2list(link) == [1, 3, 5]


def test_one_element():
    lst1 = [1]
    lst2 = [2]
    link1 = list2link(lst1)
    link2 = list2link(lst2)
    link = merge_recurision(link1, link2)
    assert link2list(link) == [1, 2]
    link1 = list2link(lst1)
    link2 = list2link(lst2)
    link = merge(link1, link2)
    assert link2list(link) == [1, 2]
    link1 = list2link(lst1)
    link2 = list2link(lst2)
    link = merge2(link1, link2)
    assert link2list(link) == [1, 2]


def test_none():
    lst1 = []
    lst2 = []
    link1 = list2link(lst1)
    link2 = list2link(lst2)
    link = merge_recurision(link1, link2)
    assert link == None
    link = merge(link1, link2)
    assert link == None
    link = merge2(link1, link2)
    assert link == None

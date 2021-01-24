from reorder_array import reorder, reorder_two_pointer, reorder_two_pointer2
from reorder_array import is_odd

def test_normal():
    lst = [1, 2, 3, 4, 5, 6, 7]
    res = reorder(lst)
    assert set(res[:4]) == set((1, 3, 5, 7))
    assert set(res[4:]) == set((2, 4, 6))
    res = reorder_two_pointer(lst)
    assert set(res[:4]) == set((1, 3, 5, 7))
    assert set(res[4:]) == set((2, 4, 6))
    res = reorder_two_pointer2(lst, is_odd)
    assert set(res[:4]) == set((1, 3, 5, 7))
    assert set(res[4:]) == set((2, 4, 6))


def test_even_odd():
    lst = [2, 4, 6, 1, 3, 5, 7]
    res = reorder(lst)
    assert set(res[:4]) == set((1, 3, 5, 7))
    assert set(res[4:]) == set((2, 4, 6))
    res = reorder_two_pointer(lst)
    assert set(res[:4]) == set((1, 3, 5, 7))
    assert set(res[4:]) == set((2, 4, 6))
    res = reorder_two_pointer2(lst, is_odd)
    assert set(res[:4]) == set((1, 3, 5, 7))
    assert set(res[4:]) == set((2, 4, 6))


def test_odd_even():
    lst = [1, 3, 5, 7, 2, 4, 6]
    res = reorder(lst)
    assert set(res[:4]) == set((1, 3, 5, 7))
    assert set(res[4:]) == set((2, 4, 6))
    res = reorder_two_pointer(lst)
    assert set(res[:4]) == set((1, 3, 5, 7))
    assert set(res[4:]) == set((2, 4, 6))
    res = reorder_two_pointer2(lst, is_odd)
    assert set(res[:4]) == set((1, 3, 5, 7))
    assert set(res[4:]) == set((2, 4, 6))


def test_odd():
    lst = [1, 3, 5]
    assert reorder(lst) == [1, 3, 5]
    assert reorder_two_pointer(lst) == [1, 3, 5]
    assert reorder_two_pointer2(lst, is_odd) == [1, 3, 5]


def test_even():
    lst = [2, 4, 6]
    assert reorder(lst) == [2, 4, 6]
    assert reorder_two_pointer(lst) == [2, 4, 6]
    assert reorder_two_pointer2(lst, is_odd) == [2, 4, 6]


def test_odd_single():
    lst = [1]
    assert reorder(lst) == [1]
    assert reorder_two_pointer(lst) == [1]
    assert reorder_two_pointer2(lst, is_odd) == [1]


def test_even_single():
    lst = [2]
    assert reorder(lst) == [2]
    assert reorder_two_pointer(lst) == [2]
    assert reorder_two_pointer2(lst, is_odd) == [2]


def test_none():
    lst = []
    assert reorder(lst) == []
    assert reorder_two_pointer(lst) == []
    assert reorder_two_pointer2(lst, is_odd) == []





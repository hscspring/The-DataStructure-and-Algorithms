from kleast_numbers import get_kleast_partition
from kleast_numbers import get_kleast
from kleast_numbers import get_kleast_heap

def test_normal():
    lst = [4, 5, 1, 3, 2]
    assert get_kleast(lst, 0) == []
    assert get_kleast(lst, 1) == [1]
    assert get_kleast(lst, 2) == [2,1]
    assert get_kleast(lst, 3) == [2,3,1]
    assert get_kleast(lst, 5) == [4,5,1,3,2]
    assert get_kleast(lst, 6) == []


def test_part_repeat():
    lst = [4, 5, 1, 6, 2, 7, 2, 8]
    assert get_kleast(lst, 0) == []
    assert get_kleast(lst, 1) == [1]
    assert get_kleast(lst, 2) == [2,1]
    assert get_kleast(lst, 3) == [2,2,1]
    assert get_kleast(lst, 5) == [4,5,1,2,2]
    assert get_kleast(lst, 9) == []

def test_multi_repeat():
    lst = [2,2,1,1,3,3]
    assert get_kleast(lst, 0) == []
    assert get_kleast(lst, 1) == [1]
    assert get_kleast(lst, 2) == [1,1]
    assert get_kleast(lst, 3) == [1,2,1]
    assert get_kleast(lst, 5) == [2,2,1,1,3]
    assert get_kleast(lst, 7) == []

def test_all_repeat():
    lst = [2,2,2,2,2,2]
    assert get_kleast(lst, 0) == []
    assert get_kleast(lst, 1) == [2]
    assert get_kleast(lst, 2) == [2,2]
    assert get_kleast(lst, 3) == [2,2,2]
    assert get_kleast(lst, 7) == []


def test_one():
    lst = [1]
    assert get_kleast(lst, 0) == []
    assert get_kleast(lst, 1) == [1]
    assert get_kleast(lst, 2) == []

def test_none():
    lst = []
    assert get_kleast(lst, 0) == []
    assert get_kleast(lst, 1) == []



def test_normal_heap():
    lst = [4, 5, 1, 3, 2]
    assert get_kleast_heap(lst, 0) == []
    assert get_kleast_heap(lst, 1) == [1]
    assert get_kleast_heap(lst, 2) == [2,1]
    assert get_kleast_heap(lst, 3) == [3,2,1]
    assert get_kleast_heap(lst, 5) == [5,4,3,2,1]
    assert get_kleast_heap(lst, 6) == []


def test_part_repeat_heap():
    lst = [4, 5, 1, 6, 2, 7, 2, 8]
    assert get_kleast_heap(lst, 0) == []
    assert get_kleast_heap(lst, 1) == [1]
    assert get_kleast_heap(lst, 2) == [2,1]
    assert get_kleast_heap(lst, 3) == [2,2,1]
    assert get_kleast_heap(lst, 5) == [5,4,2,2,1]
    assert get_kleast_heap(lst, 9) == []

def test_multi_repeat_heap():
    lst = [2,2,1,1,3,3]
    assert get_kleast_heap(lst, 0) == []
    assert get_kleast_heap(lst, 1) == [1]
    assert get_kleast_heap(lst, 2) == [1,1]
    assert get_kleast_heap(lst, 3) == [2,1,1]
    assert get_kleast_heap(lst, 5) == [3,2,2,1,1]
    assert get_kleast_heap(lst, 7) == []

def test_all_repeat_heap():
    lst = [2,2,2,2,2,2]
    assert get_kleast_heap(lst, 0) == []
    assert get_kleast_heap(lst, 1) == [2]
    assert get_kleast_heap(lst, 2) == [2,2]
    assert get_kleast_heap(lst, 3) == [2,2,2]
    assert get_kleast_heap(lst, 7) == []


def test_one_heap():
    lst = [1]
    assert get_kleast_heap(lst, 0) == []
    assert get_kleast_heap(lst, 1) == [1]
    assert get_kleast_heap(lst, 2) == []

def test_none_heap():
    lst = []
    assert get_kleast_heap(lst, 0) == []
    assert get_kleast_heap(lst, 1) == []



def test_normal_recursion():
    lst = [4, 5, 1, 3, 2]
    assert get_kleast_partition(lst, 0) == []
    assert get_kleast_partition(lst, 1) == [1]
    assert get_kleast_partition(lst, 2) == [1,2]
    assert get_kleast_partition(lst, 3) == [1,3,2]
    assert get_kleast_partition(lst, 5) == [4,1,3,2,5]
    assert get_kleast_partition(lst, 6) == []


def test_part_repeat_recursion():
    lst = [4, 5, 1, 6, 2, 7, 2, 8]
    assert get_kleast_partition(lst, 0) == []
    assert get_kleast_partition(lst, 1) == [1]
    assert get_kleast_partition(lst, 2) == [1,2]
    assert get_kleast_partition(lst, 3) == [1,2,2]
    assert get_kleast_partition(lst, 5) == [4,1,2,2,5]
    assert get_kleast_partition(lst, 9) == []

def test_multi_repeat_recursion():
    lst = [2,2,1,1,3,3]
    assert get_kleast_partition(lst, 0) == []
    assert get_kleast_partition(lst, 1) == [1]
    assert get_kleast_partition(lst, 2) == [1,1]
    assert get_kleast_partition(lst, 3) == [1,1,2]
    assert get_kleast_partition(lst, 5) == [2,2,1,1,3]
    assert get_kleast_partition(lst, 7) == []

def test_all_repeat_recursion():
    lst = [2,2,2,2,2,2]
    assert get_kleast_partition(lst, 0) == []
    assert get_kleast_partition(lst, 1) == [2]
    assert get_kleast_partition(lst, 2) == [2,2]
    assert get_kleast_partition(lst, 3) == [2,2,2]
    assert get_kleast_partition(lst, 7) == []


def test_one_recursion():
    lst = [1]
    assert get_kleast_partition(lst, 0) == []
    assert get_kleast_partition(lst, 1) == [1]
    assert get_kleast_partition(lst, 2) == []

def test_none_recursion():
    lst = []
    assert get_kleast_partition(lst, 0) == []
    assert get_kleast_partition(lst, 1) == []


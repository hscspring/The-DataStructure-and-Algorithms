from two_numbers_with_sum import find_numbers_with_sum
from two_numbers_with_sum import find_numbers_with_sum_naive


# 存在和为 s 的两个数字，这两个数字位于数组的中间
def test1():
    data = [1, 2, 4, 7, 11, 15]
    assert find_numbers_with_sum(data, 15) == [4, 11]
    assert find_numbers_with_sum_naive(data, 15) == [4, 11]


# 存在和为 s 的两个数字，这两个数字位于数组的两端
def test2():
    data = [1, 2, 4, 7, 11, 16]
    assert find_numbers_with_sum(data, 17) == [1, 16]
    assert find_numbers_with_sum_naive(data, 17) == [1, 16]


# 不存在和为 s 的两个数字
def test3():
    data = [1, 2, 4, 7, 11, 16]
    assert find_numbers_with_sum(data, 10) == []
    assert find_numbers_with_sum_naive(data, 10) == []


def test4():
    data = [1, 2]
    assert find_numbers_with_sum(data, 3) == [1, 2]
    assert find_numbers_with_sum_naive(data, 3) == [1, 2]


def test5():
    data = [1, 2]
    assert find_numbers_with_sum(data, 4) == []
    assert find_numbers_with_sum_naive(data, 4) == []


def test6():
    data = [1]
    assert find_numbers_with_sum(data, 1) == []
    assert find_numbers_with_sum_naive(data, 1) == []


def test7():
    data = [1, 2, 1, 2]
    assert find_numbers_with_sum(data, 3) == [1, 2]
    assert find_numbers_with_sum_naive(data, 3) == [1, 2]


def test8():
    data = [1, 1, 1]
    assert find_numbers_with_sum(data, 3) == []
    assert find_numbers_with_sum_naive(data, 3) == []


def test9():
    data = []
    assert find_numbers_with_sum(data, 10) == []
    assert find_numbers_with_sum_naive(data, 10) == []

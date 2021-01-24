from inverse_pairs import count_inverse_pairs
from inverse_pairs import count_inverse_pairs2

def test1():
    data = [1, 2, 3, 4, 7, 6, 5]
    assert count_inverse_pairs(data) == 3
    data = [1, 2, 3, 4, 7, 6, 5]
    assert count_inverse_pairs2(data) == 3


# 递减排序数组
def test2():
    data = [6, 5, 4, 3, 2, 1]
    assert count_inverse_pairs(data) == 15
    data = [6, 5, 4, 3, 2, 1]
    assert count_inverse_pairs2(data) == 15


# 递增排序数组
def test3():
    data = [1, 2, 3, 4, 5, 6]
    assert count_inverse_pairs(data) == 0
    data = [1, 2, 3, 4, 5, 6]
    assert count_inverse_pairs2(data) == 0


# 数组中只有一个数字
def test4():
    data = [1]
    assert count_inverse_pairs(data) == 0
    data = [1]
    assert count_inverse_pairs2(data) == 0


# 数组中只有两个数字，递增排序
def test5():
    data = [1, 2]
    assert count_inverse_pairs(data) == 0
    data = [1, 2]
    assert count_inverse_pairs2(data) == 0


# 数组中只有两个数字，递减排序
def test6():
    data = [2, 1]
    assert count_inverse_pairs(data) == 1
    data = [2, 1]
    assert count_inverse_pairs2(data) == 1


# 数组中有相等的数字
def test7():
    data = [1, 2, 1, 2, 1]
    assert count_inverse_pairs(data) == 3
    data = [1, 2, 1, 2, 1]
    assert count_inverse_pairs2(data) == 3


def test8():
    assert count_inverse_pairs([]) == 0
    assert count_inverse_pairs2([]) == 0
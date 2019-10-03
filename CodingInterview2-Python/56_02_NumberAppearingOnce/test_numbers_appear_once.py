from numbers_appear_once import find_num_appear_once


def test_normal():
    data = [2, 4, 3, 2, 5, 3, 3, 2, 5, 5]
    assert find_num_appear_once(data) == 4


def test_no_repeat():
    data = [4]
    assert find_num_appear_once(data) == 4


def test_multi_repeat():
    data = [4,  1, 1, 1, 1, 1, 1]
    assert find_num_appear_once(data) == 4


def test_only_repeat():
    data = [1, 1, 1, 2, 2, 2]
    assert find_num_appear_once(data) == None


def test_none():
    data = []
    assert find_num_appear_once(data) == None


# 所有数字都是正数，唯一的数字是最小的
def test1():
    data = [3, 3, 2, 2, 2, 3, 1]
    assert find_num_appear_once(data) == 1


# 所有数字都是正数，唯一的数字的大小位于中间
def test2():
    data = [3, 3, 2, 4, 2, 2, 3]
    assert find_num_appear_once(data) == 4


# 所有数字都是正数，唯一的数字是最大的
def test3():
    data = [4, 4, 1, 1, 1, 7, 4]
    assert find_num_appear_once(data) == 7


# 唯一的数字是负数
def test4():
    data = [-10, 214, 214, 214]
    assert find_num_appear_once(data) == -10


# 除了唯一的数字，其他数字都是负数
def test5():
    data = [-209, 3467, -209, -209]
    assert find_num_appear_once(data) == 3467


# 重复的数字有正数也有负数
def test6():
    data = [1024, -1025, 1024, -1025, 1024, -1025, 1023]
    assert find_num_appear_once(data) == 1023


# 所有数字都是负数
def test7():
    data = [-1024, -1024, -1024, -1023]
    assert find_num_appear_once(data) == -1023


# 唯一的数字是 0
def test8():
    data = [-23, 0, 214, -23, 214, -23, 214]
    assert find_num_appear_once(data) == 0


# 除了唯一的数字，其他数字都是 0
def test9():
    data = [0, 3467, 0, 0, 0, 0, 0, 0]
    assert find_num_appear_once(data) == 3467

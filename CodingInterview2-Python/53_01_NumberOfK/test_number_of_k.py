from number_of_k import get_num_ofk


# 查找的数字出现在数组的中间
def test1():
    data = [1, 2, 3, 3, 3, 3, 4, 5]
    assert get_num_ofk(data, 3) == 4


# 查找的数组出现在数组的开头
def test2():
    data = [3, 3, 3, 3, 4, 5]
    assert get_num_ofk(data, 3) == 4


# 查找的数组出现在数组的结尾
def test3():
    data = [1, 2, 3, 3, 3, 3]
    assert get_num_ofk(data, 3) == 4


# 查找的数字不存在
def test4():
    data = [1, 3, 3, 3, 3, 4, 5]
    assert get_num_ofk(data, 2) == 0


# 查找的数字比第一个数字还小，不存在
def test5():
    data = [1, 3, 3, 3, 3, 4, 5]
    assert get_num_ofk(data, 0) == 0


# 查找的数字比最后一个数字还大，不存在
def test6():
    data = [1, 3, 3, 3, 3, 4, 5]
    assert get_num_ofk(data, 6) == 0


# 数组中的数字从头到尾都是查找的数字
def test7():
    data = [3, 3, 3, 3]
    assert get_num_ofk(data, 3) == 4


# 数组中的数字从头到尾只有一个重复的数字，不是查找的数字
def test8():
    data = [3, 3, 3, 3]
    assert get_num_ofk(data, 4) == 0


# 数组中只有一个数字，是查找的数字
def test9():
    data = [3]
    assert get_num_ofk(data, 3) == 1


# 数组中只有一个数字，不是查找的数字
def test10():
    data = [3]
    assert get_num_ofk(data, 4) == 0


def test11():
    data = []
    assert get_num_ofk(data, 1) == 0

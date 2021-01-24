from missing_number import get_missing_num

# 缺失的是第一个数字 0
def test1():
    numbers = [ 1, 2, 3, 4, 5 ]
    expected = 0
    assert get_missing_num(numbers) == expected


# 缺失的是最后一个数字
def test2():
    numbers = [ 0, 1, 2, 3, 4 ]
    expected = 5
    assert get_missing_num(numbers) == expected


# 缺失的是中间某个数字 0
def test3():
    numbers = [ 0, 1, 2, 4, 5 ]
    expected = 3
    assert get_missing_num(numbers) == expected


# 数组中只有一个数字，缺失的是第一个数字 0
def test4():
    numbers = [ 1 ]
    expected = 0
    assert get_missing_num(numbers) == expected


# 数组中只有一个数字，缺失的是最后一个数字 1
def test5():
    numbers = [ 0 ]
    expected = 1
    assert get_missing_num(numbers) == expected


# 空数组
def test6():
    expected = 0;
    assert get_missing_num([]) == expected

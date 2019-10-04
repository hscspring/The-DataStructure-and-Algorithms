from max_in_sliding_window import max_in_windows, max_in_windows_list


def test1():
    data = [2, 3, 4, 2, 6, 2, 5, 1]
    expected = [4, 4, 6, 6, 6, 5]
    assert max_in_windows(data, 3) == expected
    assert max_in_windows_list(data, 3) == expected


def test2():
    data = [1, 3, -1, -3, 5, 3, 6, 7]
    expected = [3, 3, 5, 5, 6, 7]
    assert max_in_windows(data, 3) == expected
    assert max_in_windows_list(data, 3) == expected

# 输入数组单调递增


def test3():
    data = [1, 3, 5, 7, 9, 11, 13, 15]
    expected = [7, 9, 11, 13, 15]
    assert max_in_windows(data, 4) == expected
    assert max_in_windows_list(data, 4) == expected


# 输入数组单调递减
def test4():
    data = [16, 14, 12, 10, 8, 6, 4]
    expected = [16, 14, 12]
    assert max_in_windows(data, 5) == expected
    assert max_in_windows_list(data, 5) == expected

# 滑动窗口的大小为 1


def test5():
    data = [10, 14, 12, 11]
    expected = [10, 14, 12, 11]
    assert max_in_windows(data, 1) == expected
    assert max_in_windows_list(data, 1) == expected


# 滑动窗口的大小等于数组的长度
def test6():
    data = [10, 14, 12, 11]
    expected = [14]
    assert max_in_windows(data, 4) == expected
    assert max_in_windows_list(data, 4) == expected

# 滑动窗口的大小为 0


def test7():
    data = [10, 14, 12, 11]
    expected = []
    assert max_in_windows(data, 0) == expected
    assert max_in_windows_list(data, 0) == expected

# 滑动窗口的大小大于输入数组的长度


def test8():
    data = [10, 14, 12, 11]
    expected = []
    assert max_in_windows(data, 5) == expected
    assert max_in_windows_list(data, 5) == expected

# 输入数组为空


def test9():
    data = []
    expected = []
    assert max_in_windows(data, 5) == expected
    assert max_in_windows_list(data, 5) == expected

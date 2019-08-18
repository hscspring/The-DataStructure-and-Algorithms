from min_number_in_rotated_array import find_min

def test_normal():
    lst = [ 3, 4, 5, 1, 2 ]
    assert find_min(lst) == 1

def test_repeat_min():
    # 有重复数字，并且重复的数字刚好的最小的数字
    lst = [ 3, 4, 5, 1, 1, 2 ]
    assert find_min(lst) == 1

def test_repeat_not_min():
    # 有重复数字，但重复的数字不是第一个数字和最后一个数字
    lst = [ 3, 4, 5, 1, 2, 2 ]
    assert find_min(lst) == 1

def test_beg_equal_end():
    # 有重复的数字，并且重复的数字刚好是第一个数字和最后一个数字
    lst = [ 1, 0, 1, 1, 1 ]
    assert find_min(lst) == 0

def test_increase():
    # 单调升序数组，旋转 0 个元素，也就是单调升序数组本身
    lst = [ 1, 2, 3, 4, 5 ]
    assert find_min(lst) == 1

def test_single():
    # 数组中只有一个数字
    lst = [ 2 ]
    assert find_min(lst) == 2

def test_none():
    # 输入 nullptr
    assert find_min([]) == None

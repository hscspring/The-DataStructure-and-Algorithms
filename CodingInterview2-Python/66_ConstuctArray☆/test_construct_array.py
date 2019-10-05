from construct_array import build_production_array


def test1():
    # 输入数组中没有 0
    data = [ 1, 2, 3, 4, 5 ]
    expected = [ 120, 60, 40, 30, 24 ]
    assert build_production_array(data) == expected

def test2():
    # 输入数组中有一个 0
    data = [ 1, 2, 0, 4, 5 ]
    expected = [ 0, 0, 40, 0, 0 ]
    assert build_production_array(data) == expected

def test3():
    # 输入数组中有两个 0
    data = [ 1, 2, 0, 4, 0 ]
    expected = [ 0, 0, 0, 0, 0 ]
    assert build_production_array(data) == expected

def test4():
    # 输入数组中有正、负数
    data  = [ 1, -2, 3, -4, 5 ]
    expected = [ 120, -60, 40, -30, 24 ]
    assert build_production_array(data) == expected

def test5():
    # 输入输入中只有两个数字
    data  = [ 1, -2 ]
    expected = [ -2, 1 ]
    assert build_production_array(data) == expected

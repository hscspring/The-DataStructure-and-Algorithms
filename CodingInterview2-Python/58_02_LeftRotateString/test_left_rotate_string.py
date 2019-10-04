from left_rotate_string import left_rotate_string, left_rotate_string_easy


# 功能测试
def test1():
    data = "abcdefg"
    assert left_rotate_string(data, 2) == "cdefgab"
    assert left_rotate_string_easy(data, 2) == "cdefgab"

# 功能测试


def test11():
    data = "abcdefg"
    assert left_rotate_string(data, -2) == "fgabcde"
    assert left_rotate_string_easy(data, -2) == "fgabcde"

# 边界值测试


def test2():
    data = "abcdefg"
    assert left_rotate_string(data, 1) == "bcdefga"
    assert left_rotate_string_easy(data, 1) == "bcdefga"

# 边界值测试


def test22():
    data = "abcdefg"
    assert left_rotate_string(data, -1) == "gabcdef"
    assert left_rotate_string_easy(data, -1) == "gabcdef"

# 边界值测试


def test3():
    data = "abcdefg"
    assert left_rotate_string(data, 6) == "gabcdef"
    assert left_rotate_string_easy(data, 6) == "gabcdef"

# 边界值测试


def test33():
    data = "abcdefg"
    assert left_rotate_string(data, -6) == "bcdefga"
    assert left_rotate_string_easy(data, -6) == "bcdefga"

# 鲁棒性测试


def test5():
    data = "abcdefg"
    assert left_rotate_string(data, 0) == "abcdefg"
    assert left_rotate_string_easy(data, 0) == "abcdefg"

# 鲁棒性测试


def test6():
    data = "abcdefg"
    assert left_rotate_string(data, 7) == "abcdefg"
    assert left_rotate_string_easy(data, 7) == "abcdefg"

# 鲁棒性测试


def test66():
    data = "abcdefg"
    assert left_rotate_string(data, -7) == "abcdefg"
    assert left_rotate_string_easy(data, -7) == "abcdefg"

# 鲁棒性测试


def test7():
    data = "abcdefg"
    assert left_rotate_string(data, 9) == "abcdefg"
    assert left_rotate_string_easy(data, 9) == "abcdefg"

# 鲁棒性测试


def test77():
    data = "abcdefg"
    assert left_rotate_string(data, -9) == "abcdefg"
    assert left_rotate_string_easy(data, -9) == "abcdefg"


# 鲁棒性测试
def test8():
    data = ""
    assert left_rotate_string(data, 1) == ""
    assert left_rotate_string_easy(data, 1) == ""

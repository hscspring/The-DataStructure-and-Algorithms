from print_1_to_max_of_N_digits import increase, increase_recursion

def test_none():
    assert increase([]) == []

def test_0to1():
    assert increase([0]) == [1]

def test_00to01():
    assert increase([0, 0]) == [0, 1]

def test_01to02():
    assert increase([0, 1]) == [0, 2]

def test_10to11():
    assert increase([1, 0]) == [1, 1]

def test_9to10():
    assert increase([0, 9]) == [1, 0]

def test_normal_rec():
    nums = [0, 0]
    increase_recursion(nums)
    assert nums == [0, 9]

def test_none_rec():
    nums = []
    increase_recursion(nums)
    assert nums == []

def test_single0_rec():
    nums = [0]
    increase_recursion(nums)
    assert nums == [0]

def test_more_rec():
    nums = [0, 0, 0, 0]
    increase_recursion(nums)
    assert nums == [0, 9, 9, 9]
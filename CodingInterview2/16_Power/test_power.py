from power import power, power_recursion


# 底数、指数都为正数
def test_both_pos():
    assert power(2, 3) == 8
    assert power_recursion(2, 3) == 8

# 底数为负数、指数为正数
def test_base_minus_exp_pos():
    assert power(-2, 3) == -8
    assert power_recursion(-2, 3) == -8

# 指数为负数
def test_base_pos_exp_minus():
    assert power(2, -3) == 0.125
    assert power_recursion(2, -3) == 0.125

def test_both_minus():
    assert power(-2, -3) == -0.125
    assert power_recursion(-2, -3) == -0.125

# 指数为 0
def test_base_pos_exp_0():
    assert power(2, 0) == 1
    assert power_recursion(2, 0) == 1

def test_base_minus_exp_0():
    assert power(-2, 0) == 1
    assert power_recursion(-2, 0) == 1

# 底数、指数都为 0
def test_both_0():
    assert power(0, 0) == 1
    assert power_recursion(0, 0) == 1

# 底数为 0、指数为正数
def test_base0_exp_pos():
    assert power(0, 4) == 0
    assert power_recursion(0, 4) == 0

# 底数为 0、指数为负数
def test_base0_exp_minus():
    assert power(0, -4) == 0
    assert power_recursion(0, -4) == 0
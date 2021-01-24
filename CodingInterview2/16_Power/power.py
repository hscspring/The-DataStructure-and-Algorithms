"""
面试题 16：数值的整数次方
题目：实现函数 double Power (double base, int exponent)，求 base 的 exponent
次方。不得使用库函数，同时不需要考虑大数问题。

"""
import os
import sys
root_path = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_path)

from timethis import timethis

@timethis
def power(base: float, exp: int):
    """
    Calculate base ** exp.    

    Parameters
    -----------
    base: int
        Base of the expression.
    exp: int
        exponent of the expression.

    Returns
    ---------
    out: int
        base ** exp.


    Notes
    ------
    Do not need to consider the very big number.
    """
    if exp < 0 and equal_zero(base):
        return 0
    if exp < 0:
        res = 1/calc(base, -exp)
    else:
        res = calc(base, exp)
    return res


def calc(base: float, exp: int):
    if exp == 0:
        return 1
    if exp == 1:
        return base
    res = 1
    for i in range(exp):
        res *= base
    return res

@timethis
def power_recursion(base: float, exp: int):
    if exp < 0 and equal_zero(base):
        return 0
    if exp < 0:
        res = 1/calc_recursion(base, -exp)
    else:
        res = calc_recursion(base, exp)
    return res


def calc_recursion(base: float, exp: int):
    if exp == 0:
        return 1
    if exp == 1:
        return base
    # exp >> 1 == exp // 2
    res = calc_recursion(base, exp >> 1)
    res *= res
    # 4>>1 == 5>>1
    # exp & 0x1 == exp % 2
    if exp & 0x1 == 1:
        res *= base
    return res


def equal_zero(num) -> bool:
    if -1e-7 < num < 1e-7:
        return True
    else:
        return False


if __name__ == '__main__':
    res1 = power(7, 30)
    res2 = power_recursion(7, 30)
    print(res1, res2)

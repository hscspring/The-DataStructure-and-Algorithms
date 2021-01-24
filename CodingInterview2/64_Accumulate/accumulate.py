"""
面试题 64：求 1+2+…+n
题目：求 1+2+…+n，要求不能使用乘除法、for、while、if、else、switch、case
等关键字及条件判断语句（A?B:C）。
"""

from functools import reduce

def sum1(n: int) -> int:
    """
    This solution is actually a loop.

    Parameters
    -----------

    Returns
    ---------


    Notes
    ------

    """
    if n <= 0:
        return n
    return reduce(lambda x,y: x+y, range(1,n+1))


if __name__ == '__main__':
    n = 0
    res = sum1(1)
    print(res)








    
"""
面试题 65：不用加减乘除做加法
题目：写一个函数，求两个整数之和，要求在函数体内不得使用＋、－、×、÷
四则运算符号。
"""

def add(a: int, b: int) -> int:
    """
    

    Parameters
    -----------

    Returns
    ---------


    Notes
    ------

    """
    carry = 1
    while carry:
        sums = a ^ b
        carry = (a & b) << 1
        # one is positive, the other is negtive, the sum is positive
        # we need to cut off
        if carry >= 0xFFFFFFFF:
            sums = sums & 0xFFFFFFFF
            break
        a = sums
        b = carry
    return sums
    


if __name__ == '__main__':
    res = add(-1, 2)
    # res = add(2,3)
    print(res)








    
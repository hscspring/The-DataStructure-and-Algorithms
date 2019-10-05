"""
面试题 62：圆圈中最后剩下的数字
题目：0, 1, …, n-1 这 n 个数字排成一个圆圈，从数字 0 开始每次从这个圆圈里
删除第 m 个数字。求出这个圆圈里剩下的最后一个数字。
"""

def last_remaining(n: int, m: int) -> int:
    """
    

    Parameters
    -----------
    n: n nums from 0~n-1
    m: the mth num will be deleted

    Returns
    ---------
    out: the remain num.


    Notes
    ------

    """
    if n <= 0 or m <= 0:
        return -1
    lst = list(range(n))
    index = 0
    while len(lst) > 1:
        index += m - 1
        while index > len(lst) - 1:
            index -= len(lst)
        val = lst[index]
        lst.remove(val)
    return lst[0]


def last_remaining2(n: int, m: int) -> int:
    """
    n = 1: f(n, m) = 0
    n > 1: f(n, m) = (f(n-1, m) + m) % n
    """
    if n <= 0 or m <= 0:
        return -1
    last = 0
    for i in range(2, n+1):
        last = (last + m) % i
    return last



if __name__ == '__main__':
    lst = [1,2,3,4,5]
    
    res = last_remaining(5, 3)
    print(res)








    
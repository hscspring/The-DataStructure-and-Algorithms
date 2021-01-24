"""
面试题 57（二）：和为 s 的连续正数序列
题目：输入一个正数 s，打印出所有和为 s 的连续正数序列（至少含有两个数）。
例如输入 15，由于 1+2+3+4+5=4+5+6=7+8=15，所以结果打印出 3 个连续序列 1～5、
4～6 和 7～8。

"""


def find_continuous_sequence(n: int) -> list:
    """


    Parameters
    -----------
    n: the sum of continuous sequence

    Returns
    ---------
    out: the sum of the continuous of nums is equal to the given n.


    Notes
    ------

    """
    if n < 1:
        return []

    res = []
    left, right = 1, 2
    mid = (1 + n) // 2
    while left < mid:
        lst = list(range(left, right+1))
        sums = sum(lst)
        if sums == n:
            res.append(lst)
            left += 1
        elif sums < n:
            right += 1
        else:
            left += 1
    return res



def find_continuous_sequence2(n: int) -> list:
    if n < 3:
        return []

    res = []
    left, right = 1, 2
    mid = (1 + n) // 2
    sums = left + right
    while left < mid:
        if sums == n:
            res.append(list(range(left, right+1)))
        
        while sums > n and left < mid:
            sums -= left
            left += 1
            if sums == n:
                res.append(list(range(left, right+1)))

        right += 1
        sums += right
    return res

if __name__ == '__main__':
    res = find_continuous_sequence(15)
    print(res)

    res = find_continuous_sequence2(100)
    print(res)

"""
面试题 57（一）：和为 s 的两个数字
题目：输入一个递增排序的数组和一个数字 s，在数组中查找两个数，使得它们
的和正好是 s。如果有多对数字的和等于 s，输出任意一对即可

"""


def find_numbers_with_sum(lst: list, n: int) -> list:
    """


    Parameters
    -----------
    lst: the given list, sorted in order.
    n: the given num.

    Returns
    ---------
    out: two nums sum is equal to the given num.


    Notes
    ------

    """
    if len(lst) <= 1:
        return []
    left, right = 0, len(lst) - 1
    while left < right:
        two = [lst[left], lst[right]]
        sums = sum(two)
        if sums == n:
            return two
        elif sums > n:
            right -= 1
        else:
            left += 1
    return []


def find_numbers_with_sum_naive(lst: list, n: int) -> list:
    if not lst:
        return []
    for v in lst:
        if n - v in lst and (n-v != v or (n-v == v and lst.count(v) >= 2)):
            return [v, n-v]
    return []


if __name__ == '__main__':
    data = [1, 2, 4, 7, 11, 15]
    res = find_numbers_with_sum_naive(data, 15)
    print(res)

    res = find_numbers_with_sum(data, 15)
    print(res)

"""
面试题 3（二）：不修改数组找出重复的数字
题目：在一个长度为 n+1 的数组里的所有数字都在 1 到 n 的范围内，所以数组中至
少有一个数字是重复的。请找出数组中任意一个重复的数字，但不能修改输入的
数组。例如，如果输入长度为 8 的数组 {2, 3, 5, 4, 3, 2, 6, 7}，那么对应的
输出是重复的数字 2 或者 3。
"""

# 使用 list 和 dict 的方法与 find_duplication 一样，这里不再重复。
# 可以使用和 find_duplication 几乎一样的测试用例


def get_duplicate(numbers: list) -> int:
    """
    Given a list of length n+1, find the duplicated number.
    Each element is between 1 and n.
    Can not change the given list.

    Parameters
    ----------
    numbers: list
        A given number list with n+1 numbers in which each number is between 1 and n.

    Returns
    -------
    The duplicated number or None.

    Notes
    -----
    二分法，O(Nlog(N))
    """
    if not isinstance(numbers, list) or len(numbers) < 2:
        return
    res = None
    start = 1
    end = len(numbers) - 1
    while end >= start:
        middle = ((end - start) >> 1) + start
        count = count_range(numbers, start, middle)
        # if end == start and count > 1:
        #     return start
        if end == start:
            if count > 1:
                res = start
                return res
            else:
                break
        if count > middle - start + 1:
            end = middle
        else:
            start = middle + 1
    return res


def count_range(numbers, start, end):
    count = 0
    for i in numbers:
        if i >= start and i <= end:
            count += 1
    return count

if __name__ == '__main__':
    lst = [2,3,5,4,3,2,6,7]
    res = get_duplicate(lst)
    print(res)




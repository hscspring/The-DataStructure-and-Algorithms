# -*- coding: utf-8 -*-

"""
面试题 3（一）：找出数组中重复的数字
题目：在一个长度为 n 的数组里的所有数字都在 0 到 n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，
也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。例如，如果输入长度为 7 的数组 {2, 3, 1, 0, 2, 5, 3}，
那么对应的输出是重复的数字 2 或者 3。
"""

def get_duplicate1(numbers: list) -> int:
    """
    Given a list, find the duplicated number.
    Each element is between 0 and len(numbers)-1.

    Parameters
    ----------
    numbers: list
        A given number list.

    Returns
    -------
    The duplicated number or None.

    """
    if not isinstance(numbers, list) or len(numbers) < 2:
        return
    else:
        # use list
        res = None
        n = len(numbers)
        holder = [0] * n
        for i in numbers:
            if i < 0 or i > n-1:
                res = None
                break
            else:
                holder[i] += 1
                if holder[i] > 1:
                    res = i
                    break
    return res

def get_duplicate2(numbers: list) -> int:
    if not isinstance(numbers, list) or len(numbers) < 2:
        return
    else:
        # use dict
        res = None
        n = len(numbers)
        holder = {}
        for i in numbers:
            if i < 0 or i > n-1:
                res = None
                break
            else:
                if i not in holder:
                    holder[i] = 1
                else:
                    res = i
                    break
    return res


def get_duplicate3(numbers: list) -> int:
    if not isinstance(numbers, list) or len(numbers) < 2:
        return
    n = len(numbers)
    for i in numbers:
        if i < 0 or i > n-1:
            return
    for k in range(n):
        while numbers[k] != k:
            if numbers[k] == numbers[numbers[k]]:
                return numbers[k]
            tmp = numbers[k]
            numbers[k] = numbers[tmp]
            numbers[tmp] = tmp


if __name__ == '__main__':
    res = get_duplicate2([-1, -1])
    print(res)


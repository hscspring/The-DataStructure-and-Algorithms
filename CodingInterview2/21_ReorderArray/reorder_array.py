"""
面试题 21：调整数组顺序使奇数位于偶数前面
题目：输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有
奇数位于数组的前半部分，所有偶数位于数组的后半部分。

"""

def reorder(lst: list) -> list:
    return sorted(lst, key=lambda x: x%2, reverse=True)

def reorder_two_pointer(lst: list) -> list:
    """
    Reorder a list, in which odd numbers are ahead of even numbers.

    Parameters
    -----------
    lst: list
        The given list.
    Returns
    ---------
    out: list
        Reordered list.

    Notes
    ------

    """
    if not lst:
        return []
    left, right = 0, len(lst) - 1
    while left < right:
        while left < right and lst[left] & 1 == 1:
            left += 1
        while left < right and lst[right] & 1 == 0:
            right -= 1
        if left < right:
            lst[left], lst[right] = lst[right], lst[left]
    return lst


def reorder_two_pointer2(lst: list, func) -> list:
    if not lst:
        return []
    left, right = 0, len(lst) - 1
    while left < right:
        while left < right and func(lst[left]):
            left += 1
        while left < right and not func(lst[right]):
            right -= 1
        if left < right:
            lst[left], lst[right] = lst[right], lst[left]
    return lst

def is_odd(num: int):
    return num % 2


if __name__ == '__main__':
    res = reorder_two_pointer2([2,1,3,5,4,6], is_odd)
    print(res)








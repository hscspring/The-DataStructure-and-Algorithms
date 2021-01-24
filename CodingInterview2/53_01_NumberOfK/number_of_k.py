"""

面试题 53（一）：数字在排序数组中出现的次数
题目：统计一个数字在排序数组中出现的次数。例如输入排序数组 {1, 2, 3, 3,
3, 3, 4, 5} 和数字 3，由于 3 在这个数组中出现了 4 次，因此输出 4。
"""



def get_num_ofk(lst: list, num: int) -> int:
    """
    

    Parameters
    -----------
    lst: the given list
    num: the given number

    Returns
    ---------
    out: the amounts of the given num in the given list.

    Notes
    ------
    binary search + index padding
    binary search + first, last
    """
    if not lst:
        return 0
    first = get_first_k(lst, num)
    last = get_last_k(lst, num)
    if first > -1 and last > -1:
        return last - first + 1
    return 0


def get_first_k(lst: list, num: int) -> int:
    start, end = 0, len(lst) - 1
    while start <= end:
        mid = (start + end) // 2
        mid_data = lst[mid]
        if mid_data > num:
            end = mid - 1
        elif mid_data < num:
            start = mid + 1
        else:
            if mid > 0 and lst[mid-1] != num or mid == 0:
                return mid
            else:
                end = mid - 1
    return -1

def get_last_k(lst: list, num: int) -> int:
    start, end = 0, len(lst) - 1
    while start <= end:
        mid = (start + end) // 2
        mid_data = lst[mid]
        if mid_data > num:
            end = mid - 1
        elif mid_data < num:
            start = mid + 1
        else:
            if mid < end and lst[mid+1] != num or mid == end:
                return mid
            else:
                start = mid + 1
    return -1


def get_first_k_recursion(lst: list, num: int, start: int, end: int) -> int:
    if start > end:
        return -1
    mid = (start + end) // 2
    mid_data = lst[mid]
    if mid_data > num:
        end = mid - 1
    elif mid_data < num:
        start = mid + 1
    else:
        if mid > 0 and lst[mid-1] != num or mid == 0:
            return mid
        else:
            end = mid - 1
    return get_first_k_recursion(lst, num, start, end)



if __name__ == '__main__':
    lst = [3, 3, 3, 3, 4, 5]
    
    res = get_first_k(lst, 3)
    print(res)
    res = get_last_k(lst, 3)
    print(res)
    res = get_first_k_recursion(lst, 3, 0, len(lst)-1)
    print(res)

    res = get_num_ofk(lst, 3)
    print(res)












    
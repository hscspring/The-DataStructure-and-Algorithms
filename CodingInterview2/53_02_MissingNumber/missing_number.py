"""
面试题 53（二）：0 到 n-1 中缺失的数字
题目：一个长度为 n-1 的递增排序数组中的所有数字都是唯一的，并且每个数字
都在范围 0 到 n-1 之内。在范围 0 到 n-1 的 n 个数字中有且只有一个数字不在该数组
中，请找出这个数字。
"""



def get_missing_num(lst: list) -> int:
    """
    

    Parameters
    -----------
    lst: the given sorted list

    Returns
    ---------

    Notes
    ------
    binary search: lst[i] == i
    """
    start, end = 0, len(lst) - 1
    while start <= end:
        mid = (start + end) // 2
        if lst[mid] != mid:
            if mid == 0 or lst[mid-1] == mid - 1:
                return mid
            end = mid - 1
        else:
            start = mid + 1
    if start == len(lst):
        return start



if __name__ == '__main__':
    lst = [1]
    
    res = get_missing_num(lst)
    print(res)












    
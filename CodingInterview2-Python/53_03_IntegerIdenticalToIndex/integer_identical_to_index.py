"""
面试题 53（三）：数组中数值和下标相等的元素
题目：假设一个单调递增的数组里的每个元素都是整数并且是唯一的。请编程实
现一个函数找出数组中任意一个数值等于其下标的元素。例如，在数组 {-3, -1,
1, 3, 5} 中，数字 3 和它的下标相等。

"""



def get_number_same_as_index(lst: list) -> int:
    """
    

    Parameters
    -----------
    lst: the given sorted list

    Returns
    ---------

    Notes
    ------
    binary search
    """
    left, right = 0, len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == mid:
            return mid

        if lst[mid] > mid:
            right = mid - 1
        else:
            left = mid + 1
    return -1



if __name__ == '__main__':
    lst = [-3,-1,1,3,8]
    
    res = get_number_same_as_index(lst)
    print(res)












    
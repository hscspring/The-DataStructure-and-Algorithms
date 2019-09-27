"""
面试题 51：数组中的逆序对
题目：在数组中的两个数字如果前面一个数字大于后面的数字，则这两个数字组
成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。

"""



def count_inverse_pairs(lst: list) -> int:
    """
    

    Parameters
    -----------

    Returns
    ---------


    Notes
    ------

    """
    if not lst:
        return 0

    copy = lst.copy()
    count = inverse_core(lst, copy, 0, len(lst)-1)
    return count


def inverse_core(data: list, copy: list, start: int, end: int) -> int:
    if start == end:
        return 0
    mid = (end - start) // 2
    left = inverse_core(copy, data, start, start+mid)
    right = inverse_core(copy, data, start+mid+1, end)
    i = start + mid
    j = end
    index_copy = end
    count = 0

    while i >= start and j >= start + mid + 1:
        if data[i] > data[j]:
            copy[index_copy] = data[i]
            count += (j - start - mid)
            index_copy -= 1
            i -= 1
        else:
            copy[index_copy] = data[j]
            index_copy -= 1
            j -= 1

    while i >= start:
        copy[index_copy] = data[i]
        index_copy -= 1
        i -= 1
        
    while j >= start+mid+1:
        copy[index_copy] = data[j]
        index_copy -= 1
        j -= 1
    return left + right + count


def merge(left: list, right: list) -> list:
    res = []
    while  left and right:
        if left[0] <= right[0]:
            item = left.pop(0)
        else:
            item = right.pop(0)
        res.append(item)
    return res + left + right


def merge_sort(lst: list) -> list:
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(right, left)

if __name__ == '__main__':
    # lst = [7,5,6,4]
    # res = count_inverse_pairs(lst)
    # print(res)

    # left = [1,3,5]
    # right = [2,4,6]
    # left = [1, 2, 3, 8, 9]
    # right = [0, 4, 5, 6, 7]
    # res = merge(left, right)
    # print(res)

    lst = [1,3,9,8,2,5,7,6,4,0]
    res = merge_sort(lst)
    print(res)











    
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
    return inverse_core2(lst, 0, len(lst)-1)


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
    print(copy)
    return left + right + count


def inverse_core2(data: list, start: int, end: int) -> int:
    if start == end:
        return 0
    mid = (end - start) // 2
    left = inverse_core2(data, start, start+mid)
    right = inverse_core2(data, start+mid+1, end)
    i, j = start + mid, end
    tmp = []
    count = 0
    while i >= start and j >= start + mid + 1:
        if data[i] > data[j]:
            tmp.append(data[i])
            count += (j - start - mid)
            i -= 1
        else:
            tmp.append(data[j])
            j -= 1
    data[start: end+1] = data[start+mid+1:j+1] + \
        data[start:i+1] + list(reversed(tmp))
    return left + right + count


def count_inverse_pairs2(lst: list) -> int:
    if not lst:
        return 0
    return count_inversions(lst, 0, len(lst)-1)


def count_inversions(lst, start, end):
    if start == end:
        return 0
    mid = (start + end) // 2
    left = count_inversions(lst, start, mid)
    right = count_inversions(lst, mid+1, end)
    count = merge_inversions(lst, start, mid, end)
    return count + left + right


def merge_inversions(lst, start, mid, end):
    l = lst[start: mid+1] + [100000]
    r = lst[mid+1: end+1] + [100000]
    i, j = 0, 0
    count = 0
    for k in range(start, end+1):
        if l[i] <= r[j]:
            lst[k] = l[i]
            i += 1
        else:
            lst[k] = r[j]
            j += 1
            count += (mid+1-start) - i
    return count


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

    lst = [7, 5, 6, 4]
    # lst = [1, 2, 3, 4, 7, 6, 5]
    # lst = [6, 5, 4, 3, 2, 1]
    # lst = [1, 2, 1, 2, 1]

    # res = count_inverse_pairs(lst)
    # print(res)

    res = count_inverse_pairs(lst)
    print(res)

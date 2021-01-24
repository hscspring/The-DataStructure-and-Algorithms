"""
面试题 39：数组中出现次数超过一半的数字
题目：数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例
如输入一个长度为 9 的数组 {1, 2, 3, 2, 2, 2, 5, 4, 2}。由于数字 2 在数组中
出现了 5 次，超过数组长度的一半，因此输出 2。

"""

def more_than_half_num_with_dict(lst: list) -> int:
    tmp = {}
    n = len(lst)
    if not lst:
        return None
    for i in lst:
        if i in tmp:
            tmp[i] += 1
        else:
            tmp[i] = 1

        if tmp[i] > n/2:
            return i
    return 0

def more_than_half_num(lst: list) -> int:
    """
    Find the number which repeats more than half of the total numbers in the given list.

    Parameters
    -----------
    lst: the given list.

    Returns
    ---------
    out: the more than half number.

    Notes
    ------

    """
    if not lst:
        return None
    times = 1
    pre = lst[0]
    for i in lst[1:]:
        if i == pre:
            times += 1
        else:
            times -= 1
        
        if times == 0:
            pre = i
            times = 1
    if check(lst, pre):
        return pre
    return 0


def check(lst: list, pre: int) -> bool:
    k = 0
    for i in lst:
        if i == pre:
            k += 1
    return 2*k > len(lst)


def more_than_half_num_partition(lst: list) -> int:
    if not lst:
        return None
    mid, loc = len(lst)//2, 0
    lst = partition(lst, loc)
    while loc != mid:
        if loc > mid:
            loc -= 1
            lst = partition(lst, loc)
        else:
            loc += 1
            lst = partition(lst, loc)
    if check(lst, lst[mid]):
        return lst[mid]
    return 0

def partition(lst, loc):
    pi = lst[loc]
    lo = [x for x in lst if x <= pi]
    hi = [x for x in lst if x > pi]
    return lo + hi




if __name__ == '__main__':
    lst = [1, 1, 1, 1, 2, 2, 2, 2, 2]
    lst = [1, 2, 3, 2, 4, 2, 5, 2]
    lst = [1,2,2,2,2,3,4,5]
    
    res = more_than_half_num(lst)
    print(res)











    
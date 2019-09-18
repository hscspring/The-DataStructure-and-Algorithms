"""
面试题 40：最小的 k 个数
题目：输入 n 个整数，找出其中最小的 k 个数。例如输入 4、5、1、6、2、7、3、8
这 8 个数字，则最小的 4 个数字是 1、2、3、4。

"""



def get_kleast(lst: list, k: int) -> list:
    """
    get k least numbers from the given list.

    Parameters
    -----------
    lst: the given list
    k: the num of least numbers

    Returns
    ---------
    out: the k least number list


    Notes
    ------
    the container could be list, dict or tree (max heap).

    """
    if not lst or k > len(lst) or k < 1:
        return []
    container = lst[:k]
    maxc = max(container)
    index = container.index(maxc)
    for i in lst[k:]:
        if i < maxc:
            container[index] = i
            maxc = max(container)
            index = container.index(maxc)
    return container

def get_kleast_heap(lst: list, k: int) -> list:
    # also can construct all the data to a min heap.
    if not lst or k > len(lst) or k < 1:
        return []
    container = lst[:k]
    import heapq
    heapq._heapify_max(container)
    for i in lst[k:]:
        if i < container[0]:
            heapq._heapreplace_max(container, i)
    # return container
    # return sorted (convenient for testing)
    return [heapq._heappop_max(container) for i in range(k)]



def get_kleast1(lst, k):
    return sorted(lst)[:k]

def get_kleast2(lst: list, k: int) -> list:
    if not lst or k > len(lst) or k < 1:
        return []
    res = []
    for i in range(k):
        x = min(lst)
        res.append(x)
        lst.remove(x)
    return res

def get_kleast_recursion(lst: list, k: int) -> list:
    if not lst or k > len(lst) or k < 1:
        return []
    loc = 0
    lo, eq = partition(lst, loc)
    # The condition is the key point.
    while len(lo) > k or len(lo + eq) < k:
        loc += 1
        lo, eq = partition(lst, loc)
    return (lo+eq)[:k]

def partition(lst: list, loc: int) -> list:
    pi = lst[loc]
    lo, eq = [], []
    for i in lst:
        if i == pi:
            eq.append(i)
        elif i < pi:
            lo.append(i)
        else:
            continue
    return lo, eq

if __name__ == '__main__':
    lst = [4, 5, 1, 3, 2]
    lst = [4, 5, 1, 6, 2, 7, 2, 8]
    lst = [2,2,2,2,2,2]
    lst = [2,2,1,1,3,3]
    res = get_kleast_heap(lst, 5)
    print(res)












    
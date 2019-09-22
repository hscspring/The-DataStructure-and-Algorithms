"""
面试题 41：数据流中的中位数
题目：如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么
中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，
那么中位数就是所有数值排序之后中间两个数的平均值。

"""

import heapq

def get_heaps(lst: list) -> list:
    min_heap, max_heap = [], []
    n, i = 0, 0
    for v in lst:
        n += 1
        if n % 2 == 0:
            if max_heap and v < -max_heap[0]:
                v = -heapq.heapreplace(max_heap, -v)
            heapq.heappush(min_heap, v)
        else:
            if min_heap and v > min_heap[0]:
                v = heapq.heapreplace(min_heap, v)
            heapq.heappush(max_heap, -v)
    return min_heap, max_heap



def get_median(lst: list) -> int:
    """
    Get median with the given list.

    Parameters
    -----------

    Returns
    ---------


    Notes
    ------
    Use an array to store, sort.
    """

    if not lst:
        return None

    # defeat 0
    lst = [i+1e5 for i in lst]
    minh, maxh = get_heaps(lst)

    if len(lst) % 2 == 0:
        median = (minh[0] - maxh[0])/2 - 1e5
    else:
        median = -maxh[0] - 1e5

    return median







if __name__ == '__main__':
    # lst = [5, 2, 3, 4, 1, 6, 7, 0]
    # lst = [6, 3, 4, 5, 2, 7, 8, 1]
    lst = [6, 3, 4, 5, 2, 7, 8, 1]
    minh, maxh = get_heaps(lst)
    print(minh)
    print(maxh)
    print(get_median(lst))













    
"""

面试题 59（一）：滑动窗口的最大值
题目：给定一个数组和滑动窗口的大小，请找出所有滑动窗口里的最大值。例如，
如果输入数组 {2, 3, 4, 2, 6, 2, 5, 1} 及滑动窗口的大小 3，那么一共存在 6 个
滑动窗口，它们的最大值分别为 {4, 4, 6, 6, 6, 5}，

"""

from collections import deque

def max_in_windows(lst: list, width: int) -> list:
    """
    

    Parameters
    -----------

    Returns
    ---------

    Notes
    ------

    """
    res = []
    if len(lst) >= width and width >= 1:
        d = deque()
        # put the possible max num of the slide to the deque
        # storage the index instead of the real num
        for i in range(width):
            while d and lst[i] >= lst[d[-1]]:
                d.pop()
            d.append(i)
        
        for i in range(width, len(lst)):
            res.append(lst[d[0]])
            
            while d and lst[i] >= lst[d[-1]]:
                d.pop()
            d.append(i)
            # make sure d's elements are in the slide
            if d and d[0] <= i - width:
                d.popleft()
        
        res.append(lst[d[0]])
    return res
    

def max_in_windows_list(lst: list, width: int) -> list:
    res = []
    if len(lst) >= width and width >= 1:
        dq = []
        for i in range(width):
            while dq and lst[i] >= lst[dq[-1]]:
                dq.pop()
            dq.append(i)

        for i in range(width, len(lst)):
            res.append(lst[dq[0]])

            while dq and lst[i] >= lst[dq[-1]]:
                dq.pop()
            dq.append(i)

            if dq and dq[0] <= i - width:
                dq.pop(0)
        res.append(lst[dq[0]])
    return res





if __name__ == '__main__':
    lst = [2, 3, 4, 2, 6, 2, 5, 1]
    res = max_in_windows(lst, 3)
    print(res)

    res = max_in_windows_list(lst, 3)
    print(res)











    
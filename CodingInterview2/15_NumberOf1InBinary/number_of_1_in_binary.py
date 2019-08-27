"""
面试题 15：二进制中 1 的个数
题目：请实现一个函数，输入一个整数，输出该数二进制表示中 1 的个数。例如
把 9 表示成二进制是 1001，有 2 位是 1。因此如果输入 9，该函数输出 2。

"""



def num_of1_right(n: int) -> int:
    """
    Count quantity of 1 in the binary of the given int n.

    Parameters
    -----------
    n: int
        The given number.

    Returns
    ---------
    out: int
        The counts of 1 in the binary of the given number.

    Notes
    ------
    Pay attention to n < 0 case.
    O(len(n_of_binary))
    """
    count = 0
    if n < 0:
        n = -n
        # for the minus
        count = 1
    while n:
        if (n & 1):
            count += 1
        n = n >> 1
    return count

def num_of1_left(n: int) -> int:
    count = 0
    if n < 0:
        n = -n
        count = 1
    flag = 1
    while flag:
        if (n & flag):
            count += 1
        flag = flag << 1
        if flag > n:
            break
    return count

def num_of1(n: int) -> int:
    """
    一个整数减去1，与原整数做与运算，会把该整数最右边的 1 变为 0
    O(count)
    """
    count = 0
    if n < 0:
        n = -n
        count = 1
    while n:
        n = n & (n-1)
        count += 1
    return count

if __name__ == '__main__':
    res1 = num_of1_left(100)
    res2 = num_of1_right(-3)
    res3 = num_of1(100)
    print(res1, res2, res3)




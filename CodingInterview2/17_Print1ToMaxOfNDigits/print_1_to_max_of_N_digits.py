"""
面试题 17：打印 1 到最大的 n 位数
题目：输入数字 n，按顺序打印出从 1 最大的 n 位十进制数。比如输入 3，则
打印出 1、2、3 一直到最大的 3 位数即 999。

# 只需确定最大的数即可。
"""



def print_maxn_digit(n: int):
    """
    Given n, print 1 to the max number of lenth = n.
    
    Parameters
    -----------
    n: int
        Max length of the number.
    Returns
    ---------
    out: None
        Print the numbers.

    Notes
    ------
    Use array or string to solve very big number.
    It's not necessary for Python, here we just show the algorithm.
    """
    if n <= 0:
        return
    nums = [0] * (n+1)
    while not nums[0]:
        print_num(nums)
        nums = increase(nums)


def increase(nums: list):
    # is_overflow = False
    n_takeover = 0
    n_len = len(nums)
    for i in range(n_len-1, -1, -1):
        nsum = nums[i] + n_takeover
        if i == n_len - 1:
            nsum += 1
        if nsum >= 10:
            # if i == 0:
            #     is_overflow = True
            # else:
            nsum -= 10
            n_takeover = 1
            nums[i] = nsum
        else:
            nums[i] = nsum
            break
    return nums

def print_num(nums:list):
    res = []
    is_begining = True
    for i in nums:
        if is_begining and i != 0:
            is_begining = False
        if not is_begining:
            res.append(i)
    print("".join('{0}'.format(i) for i in res))


def print_maxn_digit_recursion(n: int):
    if n <= 0:
        return
    nums = [0] * (n+1)
    # for i in range(10):
    #     nums[0] = i
    increase_recursion(nums)

def increase_recursion(nums: list, index=0):
    if len(nums) < 2:
        return
    if index == len(nums) - 1:
        print_num(nums)
        return
    for i in range(10):
        nums[index+1] = i
        increase_recursion(nums, index+1)




if __name__ == '__main__':
    # res = print_maxn_digit(2)
    # nums = [0] * 3
    # increase_recursion(nums, 0)
    print_maxn_digit_recursion(2)
    print_maxn_digit(2)





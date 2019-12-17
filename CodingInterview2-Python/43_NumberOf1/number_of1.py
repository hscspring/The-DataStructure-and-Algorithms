"""
面试题 43：从 1 到 n 整数中 1 出现的次数
题目：输入一个整数 n，求从 1 到 n 这 n 个整数的十进制表示中 1 出现的次数。例如
输入 12，从 1 到 12 这些整数中包含 1 的数字有 1，10，11 和 12，1 一共出现了 5 次。
"""



def number_of_one(n: int) -> int:
    """
    how many ones between 1 to n.

    Parameters
    -----------

    Returns
    ---------


    Notes
    ------
    given number n, we have log(n) positions

    """
    res = 0
    for i in range(1, n+1):
        res += number_one(i)
    return res


def number_one(n: int):
    res = 0
    while n:
        if n%10 == 1:
            res += 1
        n = n//10
    return res


def len_num(n: int) -> int:
    res = 0
    while n:
        res += 1
        n //= 10
    return res

def first_num(n: int) -> int:
    while n >= 10:
        n //= 10
    return n


def number_of_one_recursion(n: int) -> int:

    lenth = len_num(n)
    first = first_num(n)
    nums_first = 0

    if lenth == 0 or first == 0:
        return 0

    # 21345
    if lenth == 1 and first > 0:
        return 1

    # 10000-19999 的第一个位中 1 的数目
    if lenth > 1 and first > 1:
        nums_first = 10 ** (lenth - 1)
    
    elif lenth > 1 and first == 1:
        nums_first = n - 10 ** (lenth - 1) + 1

    # 01346-21345 除了第一位之外的数位中 1 的数目
    # 排列组合
    nums_other = first * (lenth - 1) * 10 ** (lenth - 2)
    
    # 1-1345 中 1 的数目
    nums_recur = number_of_one_recursion(n % 10**(lenth-1))
    
    return nums_first + nums_other + nums_recur



def count_one(num):
    str_lst = map(str, range(1, num+1))
    return "".join(str_lst).count("1")


if __name__ == '__main__':
    num = 100
    num = 2134522

    import time
    t0 = time.time()
    res = number_of_one_recursion(num)
    print(res)
    print(time.time()-t0)

    t0 = time.time()
    res = count_one(num)
    print(res)
    print(time.time()-t0)

    t0 = time.time()
    res = number_of_one(num)
    print(res)
    print(time.time()-t0)













    
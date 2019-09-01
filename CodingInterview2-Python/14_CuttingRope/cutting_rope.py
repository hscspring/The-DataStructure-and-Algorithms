"""
面试题 14：剪绳子
题目：给你一根长度为 n 绳子，请把绳子剪成 m 段（m、n 都是整数，n>1 并且 m≥1）。
每段的绳子的长度记为 k [0]、k [1]、……、k [m]。k [0]*k [1]*…*k [m] 可能的最大乘
积是多少？例如当绳子的长度是 8 时，我们把它剪成长度分别为 2、3、3 的三段，此
时得到最大的乘积 18。

"""

def max_production_dp(n: int) -> int:
    """
    Given a number n, divided to m parts, 
    Return the biggest production of all the parts.

    Parameters
    -----------
    n: int
        The length of the given rope, also could treat as a number.

    Returns
    ---------
    out: int
        The biggest production of all the divided m parts.

    Notes
    ------

    """
    if n < 2:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 2
    
    products = [0, 1, 2, 3] + [0] * (n-3)
    for i in range(4, n+1):
        mx = 0
        for j in range(1, i//2+1):
            product = products[j] * products[i-j]
            if mx < product:
                mx = product
        products[i] = mx
    return products[-1]


def max_production_greedy(n: int) -> int:
    if n < 2:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 2

    n3 = n//3
    remain = n - n3*3
    if remain == 1:
        res = 3 ** (n3-1) * 4
    elif remain == 2:
        res = 3 ** n3 * 2
    else:
        res = 3 ** n3

    return res


if __name__ == '__main__':
    res = max_production(8)
    print(res)



"""
面试题 10：斐波那契数列
题目：写一个函数，输入 n，求斐波那契（Fibonacci）数列的第 n 项。

"""

def fib_recursion(n: int) -> int:
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

def fib_loop(n: int) -> int:
    # store the calculated ones
    if n <= 0:
        return 0
    if n == 1:
        return 1
    tmp = [0, 1]
    for i in range(2, n+1):
        res = sum(tmp)
        tmp = [tmp[-1], res]
    return res

def fib(n: int):
    res = [0,1]
    if n < 2:
        return res[n]
    f, s, fn = 0, 1, 0
    for i in range(2, n+1):
        fn = f + s
        f = s
        s = fn
    return fn


def fib_matrix(n: int) -> int:
    """
    [[f(n), f(n-1)], [f(n-1), f(n-2)]] = [[1, 1], [1, 0]] ^(n-1)
    a^n = a^{n/2} a^{n/2} when n is even
    a^n = a^{(n-1)/2} a^{(n-1)/2} a when n is odd
    """
    if n < 2: return [0, 1][n]
    return matrix_power([[1, 1], [1, 0]], n-1)[0][0]

def matrix_multiply(m1: [list], m2: [list]) -> [list]:
    n00 = m1[0][0] * m2[0][0] + m1[0][1] * m2[1][0]
    n01 = m1[0][0] * m2[0][1] + m1[0][1] * m2[1][1]
    n10 = m1[1][0] * m2[0][0] + m1[1][1] * m2[1][0]
    n11 = m1[1][0] * m2[0][1] + m1[1][1] * m2[1][1]
    return [[n00, n01], [n10, n11]]

def matrix_power(base: [list], exp: int):
    if exp == 1:
        matrix = base
    elif exp > 1 and exp % 2 == 0:
        matrix = matrix_power(base, exp/2)
        matrix = matrix_multiply(matrix, matrix)
    elif exp > 1 and exp % 2 == 1:
        matrix = matrix_power(base, (exp-1)/2)
        matrix = matrix_multiply(base, matrix_multiply(matrix, matrix))
    else:
        matrix = [[0, 0], [0, 0]]
        print("exp invalid")
    return matrix


import numpy as np
def fib2(n):
    if n < 2:
        return [0, 1][n]
    base = np.array([[1, 1], [1, 0]])
    res = base
    for i in range(2, n):
        res = np.dot(base, res)
    return res[0][0]

import numpy as np
def fib3(n):
    if n < 2:
        return [0, 1][n]
    base = np.array([[1, 1], [1, 0]])
    return matrix_multiply(base, n-1)[0][0]

def matrix_multiply(base, exp):
    if exp == 1:
        res = base
    elif exp > 1 and exp % 2 == 0:
        res = matrix_multiply(base, exp/2)
        res = np.dot(res, res)
    elif exp > 1 and exp % 2 == 1:
        res = matrix_multiply(base, (exp-1)/2)
        res = np.dot(res, res).dot(base)
    else:
        res = base
    return res

if __name__ == '__main__':
    print(fib_loop(40))
    # print(fib(40))
    # print(fib_matrix(40))
    # print(fib_matrix(-2))
    print(fib2(40))
    print(fib3(40))




"""
题目：输入一个由正整数组成的数组和一个正整数k，请问数组中有多少个数字乘积小于k的连续子数组？例如，输入数组[10，5，2，6]，k的值为100，有8个子数组的所有数字的乘积小于100，它们分别是[10]、[5]、[2]、[6]、[10，5]、[5，2]、[2，6]和[5，2，6]。
"""

inp = [10, 5, 2, 6]
k = 100


def run(inp, k):
    res = 0
    p1 = 0
    prod = 1
    for p2, v in enumerate(inp):
        prod *= v
        while p1 <= p2 and prod >= k:
            prod /= inp[p1]
            p1 += 1
        if p2 >= p1:
            res += (p2 - p1 + 1)
    return res


res = run(inp, k)
print(res)

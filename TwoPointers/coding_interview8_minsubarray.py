"""
题目：输入一个正整数组成的数组和一个正整数k，请问数组中和大于或等于k的连续子数组的最短长度是多少？如果不存在所有数字之和大于或等于k的子数组，则返回0。例如，输入数组[5，1，4，3]，k的值为7，和大于或等于7的最短连续子数组是[4，3]，因此输出它的长度2。
"""

inp = [5, 1, 4, 3]
k = 7


def run(inp, k):
    p1 = 0
    p2 = 1
    length = len(inp)
    res = 1e9
    while p2 < length:
        x = sum(inp[p1: p2])
        while p2 < length and x < k:
            x += inp[p2]
            p2 += 1
        while p1 < p2 and x >= k:
            x -= inp[p1]
            p1 += 1
            _len = (p2 - p1 + 1)
            res = min(res, _len)
    return res


def run2(inp, k):
    p1 = 0
    add = 0
    res = 1e9
    for p2, v in enumerate(inp):
        add += v
        while p1 <= p2 and add >= k:
            res = min(res, p2 - p1 + 1)
            add -= inp[p1]
            p1 += 1
    return res


res = run(inp, k)
print(res)

assert run(inp, 3) == 1
assert run(inp, 10) == 3
assert run(inp, 8) == 3
assert run(inp, 9) == 3

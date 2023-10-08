"""
题目：输入一个整数数组和一个整数k，请问数组中有多少个数字之和等于k的连续子数组？例如，输入数组[1，1，1]，k的值为2，有2个连续子数组之和等于2。
"""

inp = [1, 1, 1]
k = 2


def run(inp, k):
    dct = {0: 1}
    add = 0
    count = 0
    for v in inp:
        add += v
        count += dct.get(add - k, 0)
        dct[add] = dct.get(add, 0) + 1
    return count


res = run(inp, k)
print(res)


assert run([4, 1, 5, 2, 3], 5) == 3

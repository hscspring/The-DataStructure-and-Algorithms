"""
题目：输入一个数组，如何找出数组中所有和为0的3个数字的三元组？需要注意的是，返回值中不得包含重复的三元组。例如，在数组[-1，0，1，2，-1，-4]中有两个三元组的和为0，它们分别是[-1，0，1]和[-1，-1，2]。
"""

inp = [-1, 0, 1, 2, -1, -4]


def twosum(inp, k):
    i = k + 1
    j = len(inp) - 1
    res = []
    while i < j:
        x = inp[k] + inp[i] + inp[j]
        if x == 0:
            res.append((inp[k], inp[i], inp[j]))
            i += 1
            j -= 1
        elif x < 0:
            i += 1
        else:
            j -= 1
    return res


def run(inp):
    inp = sorted(inp)
    res = []
    i = 0
    while i < len(inp) - 2:
        for v in twosum(inp, i):
            res.append(v)
        tmp = inp[i]
        while i < len(inp) and tmp == inp[i]:
            i += 1
    return res


res = run(inp)
print(res)

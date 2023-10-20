"""
题目：给定一个没有重复数字的正整数集合，请找出所有元素之和等于某个给定值的所有组合。同一个数字可以在组合中出现任意次。例如，输入整数集合[2，3，5]，元素之和等于8的组合有3个，分别是[2，2，2，2]、[2，3，3]和[3，5]。
"""


def run(inp, k):
    combs = []
    res = []
    core(inp, k, 0, combs, res)
    return res


def core(arr, target, i, combs, res):
    add = sum(combs)
    if add == target:
        res.append(combs.copy())
    elif add < target and i < len(arr):
        core(arr, target, i + 1, combs, res)
        combs.append(arr[i])
        core(arr, target, i, combs, res)
        combs.pop()


inp = [2, 3, 5]
k = 8
res = run(inp, k)
print(res)

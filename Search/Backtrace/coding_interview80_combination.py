"""
题目：输入n和k，请输出从1到n中选取k个数字组成的所有组合。例如，如果n等于3，k等于2，将组成3个组合，分别是[1，2]、[1，3]和[2，3]。
"""


def run(n, k):
    res = []
    combines = []
    core(n, k, 1, combines, res)
    return res


def core(n, k, i, combs, res):
    if len(combs) == k:
        res.append(combs.copy())
    elif i <= n:
        core(n, k, i + 1, combs, res)
        combs.append(i)
        core(n, k, i + 1, combs, res)
        combs.pop()


res = run(3, 2)
print(res)

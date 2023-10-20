"""
题目：输入一个不含重复数字的数据集合，请找出它的所有子集。例如，数据集合[1，2]有4个子集，分别是[]、[1]、[2]和[1，2]。
"""


def run(inp):
    res = []
    if not inp:
        return res
    core(inp, 0, [], res)
    return res


def core(arr, idx, subset, res):
    if idx == len(arr):
        res.append(subset.copy())
    elif idx < len(arr):
        core(arr, idx + 1, subset, res)

        subset.append(arr[idx])
        core(arr, idx + 1, subset, res)
        subset.pop()


inp = [1, 2, 3]
res = run(inp)
print(res)

"""
给定一个无重复元素的数组nums和一个目标数sum，输出所有使数字和为目标数的组合。
"""


def run(inp, n):

    res = []
    inp = sorted(inp, key=lambda x: -x)
    length = len(inp)

    def core(curr_sum, solution, idx):
        if curr_sum > n:
            return
        if curr_sum == n:
            res.append(solution)
        for i in range(idx, length):
            new_sum = curr_sum + inp[i]
            new_sol = solution + [inp[i]]
            core(new_sum, new_sol, i)

    core(0, [], 0)
    return res


nums = [3, 5, 2, 6]
n = 9
res = run(nums, n)
print(res)



def run(inp, k):

    res = []

    def core(inp, solution):
        if len(solution) == k:
            res.append(solution)
        for i in range(len(inp)):
            new_sol = solution + [inp[i]]
            new_inp = inp[i + 1:]
            core(new_inp, new_sol)
    core(inp, [])
    return res


nums = [1, 2, 3, 4, 5]
k = 3
res = run(nums, k)
print(res)

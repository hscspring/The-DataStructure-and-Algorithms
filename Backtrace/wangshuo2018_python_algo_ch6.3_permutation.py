def run(inp):

    res = []

    def core(inp, solution):
        if len(inp) == 0:
            res.append(solution)
        for i in range(len(inp)):
            new_sol = solution + [inp[i]]
            new_inp = inp[:i] + inp[i + 1:]
            core(new_inp, new_sol)
    core(inp, [])
    return res


inp = ["a", "b", "c"]
res = run(inp)
print(res)

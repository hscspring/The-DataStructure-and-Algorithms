"""
给定n种物品和一个背包。物品i的重量是wi，其价值为vi，背包的容量为C。问应如何选择装入背包的物品，使得装入背包中物品的总价值最大?
"""


def run(ws, vs, c):
    dp = [0] * (c + 1)
    for i in range(len(ws)):
        for j in range(c, -1, -1):
            if j >= ws[i]:
                ans = dp[j - ws[i]] + vs[i]
                if dp[j] < ans:
                    dp[j] = ans
    print(dp)
    return dp[c]


weights = [4, 3, 2]
values = [5, 4, 1]
c = 6

res = run(weights, values, c)
print(res)

"""
题目：一个机器人从m×n的格子的左上角出发，它每步要么向下要么向右，直到抵达格子的右下角。请计算机器人从左上角到达右下角的路径的数目。例如，如果格子的大小是3×3，那么机器人从左上角到达右下角有6条符合条件的不同路径，如图14.7所示。
"""


def run(m, n):
    dp = []
    for i in range(m):
        tmp = []
        for j in range(n):
            tmp.append(0)
        dp.append(tmp)
    for i in range(m):
        dp[i][0] = 1
    for j in range(n):
        dp[0][j] = 1

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[m - 1][n - 1]


res = run(3, 3)
print(res)

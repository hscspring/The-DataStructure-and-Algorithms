"""
给定n个数字矩阵A1,A2,⋅⋅⋅,An，其中，Ai与Ai+1（i=1,2,⋅⋅⋅,n）是可乘的。用加括号的方式表示矩阵连乘的次序，不同加括号的方法所对应的计算次序是不同的，所需要的数乘次数也不一样。
"""

from utils import print_dp


def run(dims, num):
    length = len(dims)
    dp = [[0] * length for _ in range(length)]
    # 长度len的矩阵链最优值
    for _len in range(2, num + 1):
        # 开始下标
        for i in range(1, num - _len + 1 + 1):
            # 结束下标
            j = i + _len - 1
            dp[i][j] = 1e9
            # 枚举划分位置
            for k in range(i, j):
                ans = dp[i][k] + dp[k + 1][j] + dims[i - 1] * dims[k] * dims[j]
                if ans < dp[i][j]:
                    dp[i][j] = ans
    print_dp(dp)
    return dp[1][length - 1]


# 3 matrix
inp = [10, 100, 5, 50]
res = run(inp, 3)
print(res)

# 6 matrix
inp = [30, 35, 15, 5, 10, 20, 25]
res = run(inp, 6)
print(res)

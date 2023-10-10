"""
问题描述：若给定序列X={x1,x2,…,xm}和Z={z1,z2,…,zk}，若Z是X的子序列，当且仅当存在一个严格递增下标序列{i1,i2,…,ik}，使得对于所有j=1,2,…,k有zj=xij。例如，序列Z={B, C, D, B}是序列X={A, B, C, B, D, A, B}的子序列，相应的递增下标序列为{2, 3, 5, 7}。
"""

from utils import print_dp


def run(a, b):
    len1 = len(a) + 1
    len2 = len(b) + 1
    dp = [[0] * len2 for _ in range(len1)]
    for i in range(1, len1):
        for j in range(1, len2):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    print_dp(dp)
    return dp[len1 - 1][len2 - 1]


a = "ABCBDAB"
b = "CBCEDB"

res = run(a, b)
print(res)


def lcstring(a, b):
    len1 = len(a) + 1
    len2 = len(b) + 1
    dp = [[0] * len2 for _ in range(len1)]
    res = -1
    for i in range(1, len1):
        for j in range(1, len2):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            if dp[i][j] > res:
                res = dp[i][j]
    print_dp(dp)
    return res


a = "abcdef"
b = "bcdefaaa"
res = lcstring(a, b)
print(res)

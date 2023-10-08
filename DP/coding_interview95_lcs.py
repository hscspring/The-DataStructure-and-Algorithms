"""
题目：输入两个字符串，请求出它们的最长公共子序列的长度。如果从字符串s1中删除若干字符之后能得到字符串s2，那么字符串s2就是字符串s1的一个子序列。例如，从字符串"abcde"中删除两个字符之后能得到字符串"ace"，因此字符串"ace"是字符串"abcde"的一个子序列。但字符串"aec"不是字符串"abcde"的子序列。如果输入字符串"abcde"和"badfe"，那么它们的最长公共子序列是"bde"，因此输出3。
"""


def lcs(s1, s2):
    len1 = len(s1)
    len2 = len(s2)
    dp = [[0] * (len2 + 1) for i in range(len1 + 1)]
    for i in range(len1):
        for j in range(len2):
            if s1[i] == s2[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
    return dp[len1][len2]


a = "abcde"
b = "badfe"
res = lcs(a, b)
print(res)

a = "abcdefg"
b = "abdeghk"
res = lcs(a, b)
print(res)

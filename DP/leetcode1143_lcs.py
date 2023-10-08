"""
给定两个字符串 text1 和 text2，返回这两个字符串的最长 公共子序列 的长度。如果不存在 公共子序列 ，返回 0 。

一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。

例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。
两个字符串的 公共子序列 是这两个字符串所共同拥有的子序列。



示例 1：

输入：text1 = "abcde", text2 = "ace"
输出：3
解释：最长公共子序列是 "ace" ，它的长度为 3 。
示例 2：

输入：text1 = "abc", text2 = "abc"
输出：3
解释：最长公共子序列是 "abc" ，它的长度为 3 。
示例 3：

输入：text1 = "abc", text2 = "def"
输出：0
解释：两个字符串没有公共子序列，返回 0 。
"""


def longest_common_substring(s1, s2):
    """
    # 最长公共子串（序列是连续的）
    给定两个字符串 str1 和 str2, 输出两个字符串的最长公共子串
    题目保证 str1 和 str2 的最长公共子串存在且唯一。
    """
    l1, l2 = len(s1), len(s2)
    dp = [[0] * (l2 + 1) for i in range(l1 + 1)]
    res = ""
    for i in range(1, l1 + 1):
        for j in range(1, l2 + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            if dp[i][j] > len(res):
                res = s1[i - dp[i][j]: i]
    return res


def longest_common_sequence(s1, s2):
    """
    # 最长公共子序列（序列可能不连续）
    给定两个字符串 str1 和 str2，输出两个字符串的最长公共子序列。
    目前给出的数据，仅仅会存在一个最长的公共子序列
    """
    l1, l2 = len(s1), len(s2)
    dp = [[""] * (l2 + 1) for i in range(l1 + 1)]
    for i in range(1, l1 + 1):
        for j in range(1, l2 + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + s1[i - 1]
            else:
                if len(dp[i - 1][j]) > len(dp[i][j - 1]):
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i][j - 1]
    return dp[-1][-1]


a = "abcdefg"
b = "abdeghk"

res1 = longest_common_substring(a, b)
print(res1)
res2 = longest_common_sequence(a, b)
print(res2)

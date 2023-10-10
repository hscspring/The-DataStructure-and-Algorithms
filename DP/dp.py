def max_profit(ps):
    """
    # 买卖股票的最好时机
    假设你有一个数组，其中第 i 个元素是股票在第 i 天的价格。
    你可以买入一次股票和卖出一次股票（并非每天都可以买入或卖出一次，总共只能买入和卖出一次），问能获得的最大收益是多少。
    """
    mi, ma, res = 1e5, 0, 0
    for v in ps:
        if v < mi:
            mi = v
        if v > ma:
            ma = v
        p = v - mi
        if p > res:
            res = p
    return res


def min_path_sum(arr):
    """
    # 矩阵最小路径和
    给定一个 n * m 的矩阵 a，从左上角开始每次只能向右或者向下走，最后到达右下角的位置，
    路径上所有的数字累加起来就是路径和，输出所有的路径中最小的路径和。
    """
    if not arr or not arr[0]:
        return 0
    r, c = len(arr), len(arr[0])
    dp = [[0] * c for i in range(r)]
    dp[0][0] = arr[0][0]
    for i in range(1, r):
        dp[i][0] = dp[i - 1][0] + arr[i][0]
    for i in range(1, c):
        dp[0][i] = dp[0][i - 1] + arr[0][i]
    for i in range(1, r):
        for j in range(1, c):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + arr[i][j]
    return dp[-1][-1]


def min_edit_cost(s1, s2, ic, dc, rc):
    """
    # 最小编辑代价
    给定两个字符串 str1 和 str2，再给定三个整数 ic，dc 和 rc，分别代表插入、删除和替换一个字符的代价，
    请输出将 str1 编辑成 str2 的最小代价。
    """
    l1, l2 = len(s1), len(s2)
    if not s1:
        return l2 * ic
    if not s2:
        return l1 * dc
    dp = [[0] * (l2 + 1) for i in range(l1 + 1)]
    for i in range(l1 + 1):
        dp[i][0] = i * dc
    for i in range(l2 + 1):
        dp[0][i] = i * ic
    for i in range(1, l1 + 1):
        for j in range(1, l2 + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(
                    dp[i - 1][j] + dc, dp[i][j - 1] + ic, dp[i - 1][j - 1] + rc
                )
    return dp[-1][-1]


def longest_palindrome_substring(s):
    """
    # 最长回文子串（解法一）
    对于一个字符串（仅包含小写英文字母），请设计一个高效算法，计算其中最长回文子串的长度。
    给定字符串 A 以及它的长度 n ，请返回最长回文子串的长度。
    """
    def func(s, le, ri):
        while le >= 0 and ri < len(s) and s[le] == s[ri]:
            le -= 1
            ri += 1
        return ri - le - 1

    res = 0
    for i in range(len(s)):
        res = max(res, func(s, i, i), func(s, i, i + 1))
    return res


def longest_palindrome_substring2(s):
    """
    # 最长回文子串（解法二）
    对于一个字符串（仅包含小写英文字母），请设计一个高效算法，计算其中最长回文子串的长度。
    给定字符串 A 以及它的长度 n ，请返回最长回文子串的长度。
    """
    res = 0
    n = len(s)
    dp = [[0] * n for i in range(n)]
    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            dp[i][j] = s[i] == s[j] and (j - i < 3 or dp[i + 1][j - 1])
            if dp[i][j] and j - i + 1 > res:
                res = j - i + 1
    return res

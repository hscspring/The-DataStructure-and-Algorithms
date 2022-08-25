def permutation(s):
    """
    # 字符串排列
    输入一个长度为 n 字符串，打印出该字符串中字符的所有排列，你可以以任意顺序返回这个字符串数组。
    例如输入字符串 ABC, 则输出由字符 A,B,C 所能排列出来的所有字符串 ABC,ACB,BAC,BCA,CBA 和 CAB。
    """
    res = []
    def func(pre, suf):
        if not suf:
            res.append(pre)
        for i in range(len(suf)):
            func(pre+suf[i], suf[:i]+suf[i+1:])
    func("", s)
    return res


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


def greatest_sum_of_subarrays(arr):
    """
    # 连续子数组最大和
    输入一个长度为 n 的整型数组 a，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。
    """
    if not arr:
        return 0
    lm, gm = 0, arr[0]
    for v in arr:
        if lm < 0:
            lm = v
        else:
            lm += v
        if lm > gm:
            gm = lm
    return gm


def unique_path(m, n):
    """
    # 求路径
    一个机器人在 m×n 大小的地图的左上角（起点）。
    机器人每次可以向下或向右移动。机器人要到达地图的右下角（终点）。
    可以有多少种不同的路径从起点走到终点？
    """
    dp = [[0] * (n) for i in range(m)]
    for i in range(m):
        dp[i][0] = 1
    for i in range(n):
        dp[0][i] = 1
    for i in range(m):
        for j in range(n):
            dp[i][j] = dp[i - 1][j] + dp[i][j + 1]
    return dp[-1][-1]


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
            if s1[i - 1] == s2[i - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(
                    dp[i - 1][j] + dc, dp[i][j - 1] + ic, dp[i - 1][j - 1] + rc
                )
    return dp[-1][-1]


def longest_common_substring(s1, s2):
    """
    # 最长公共子串
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
                res = s1[i - dp[i][j] : i]
    return res


def longest_common_sequence(s1, s2):
    """
    # 最长公共子序列
    给定两个字符串 str1 和 str2，输出两个字符串的最长公共子序列。
    目前给出的数据，仅仅会存在一个最长的公共子序列
    """
    l1, l2 = len(s1), len(s2)
    dp = [[""] * (s2 + 1) for i in range(l1 + 1)]
    for i in range(1, l1 + 1):
        for j in range(2, l2 + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + s1[i]
            else:
                dp[i][j] = (
                    dp[i - 1][j]
                    if len(dp[i - 1][j]) > len(dp[i][j - 1])
                    else dp[i][j - 1]
                )
    return dp[-1][-1]


def longest_palindrome_substring(s):
    """
    # 最长回文子串（解法一）
    对于一个字符串（仅包含小写英文字母），请设计一个高效算法，计算其中最长回文子串的长度。
    给定字符串 A 以及它的长度 n ，请返回最长回文子串的长度。
    """
    def func(s, l, r):
        while l>=0 and r<len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return r - l - 1

    res = 0
    for i in range(len(s)):
        res = max(res, func(s, i, i), func(s, i, i+1))
    return res


def longest_palindrome_substring(s):
    """
    # 最长回文子串（解法二）
    对于一个字符串（仅包含小写英文字母），请设计一个高效算法，计算其中最长回文子串的长度。
    给定字符串 A 以及它的长度 n ，请返回最长回文子串的长度。
    """
    res = 0
    n = len(s)
    dp = [[0] * n for i in range(n)]
    for i in range(n-1, -1, -1):
        for j in range(i, n):
            dp[i][j] = s[i] == s[j] and (j - i < 3 or dp[i+1][j-1])
            if dp[i][j] and j - i + 1 > res:
                res = j - i + 1
    return res



"""
题目：输入一个字符串，求该字符串中不含重复字符的最长子字符串的长度。例如，输入字符串"babcca"，其最长的不含重复字符的子字符串是"abc"，长度为3。
"""

inp = "babcca"


def has_repeat(s):
    return len(set(s)) != len(s)


def run(inp):
    p1 = 0
    res = -1
    for p2 in range(1, len(inp)):
        sub = inp[p1:p2]
        while p1 < p2 and has_repeat(sub):
            p1 += 1
            sub = inp[p1:p2]
        res = max(res, len(sub))
    return res


res = run(inp)
print(res)

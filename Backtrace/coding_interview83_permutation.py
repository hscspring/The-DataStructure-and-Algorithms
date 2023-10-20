def permutate(s):
    res = []
    permutate_core(s, 0, res)
    return res


def permutate_core(s, i, res):
    if i == len(s):
        res.append("".join(s))
    else:
        for j in range(i, len(s)):
            swap(s, i, j)
            permutate_core(s, i + 1, res)
            swap(s, i, j)


def swap(s, i, j):
    if i != j:
        tmp = s[i]
        s[i] = s[j]
        s[j] = tmp


def permutation(s):
    """
    # 字符串排列
    输入一个长度为 n 字符串，打印出该字符串中字符的所有排列，你可以以任意顺序返回这个字符串数组。
    例如输入字符串 ABC, 则输出由字符 A,B,C 所能排列出来的所有字符串 ABC,ACB,BAC,BCA,CBA 和 CAB。
    """
    # https://www.youtube.com/watch?v=IPWmrjE1_MU
    res = []

    def func(suf, pre):
        if not suf:
            res.append(pre)
        for i in range(len(suf)):
            func(pre + suf[i], suf[:i] + suf[i + 1:])
    func(s, "")
    return res



inp = ["a", "b", "c"]
res1 = permutate(inp)
print(res1)
res2 = permutation("abc")
print(res2)



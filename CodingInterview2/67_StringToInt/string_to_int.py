"""
面试题 67：把字符串转换成整数
题目：请你写一个函数 StrToInt，实现把字符串转换成整数这个功能。当然，不
能使用 atoi 或者其他类似的库函数。
"""


def str2int(s: str) -> int:
    """

    Parameters
    -----------

    Returns
    ---------


    Notes
    ------

    """

    nums = set("1 2 3 4 5 6 7 8 9".split())
    oper = set(("+", "-"))

    minus = 0
    # s is ""
    if not s:
        status = "invalid"
        print(status)
        return 0

    if s[0] in oper:

        i = 1
        while i < len(s):
            if s[i] not in oper:
                break
            i += 1

        # like +, ++
        if len(s[i:]) == 0:
            status = "invalid"
            print(status)
            return 0

        # like +01
        if s[i] == "0":
            for w in s[i:]:
                if w != 0:
                    status = "invalid"
                    print(status)
                    return 0
            return 0
        else:
            for w in s[:i]:
                if w == "-":
                    minus += 1
            return toint(s[i:], minus % 2)

    if s[0] == "0":
        for w in s[1:]:
            if w != "0":
                status = "invalid"
                print(status)
                return 0
        return 0
    return toint(s, False)


def toint(s: str, minus: bool) -> int:
    nums = set("1 2 3 4 5 6 7 8 9".split())
    for w in s:
        if w not in nums and w != "0":
            status = "invalid"
            print(status)
            return 0

    lenth = len(s)
    num = 0
    for w in s:
        num += int(w) * 10 ** (lenth-1)
        # if minus:
        #     if -num < -0x80000000:
        #         return 0
        # else:
        #     if num > 0x7FFFFFFF:
        #         return 0
        lenth = lenth - 1

    if minus:
        res = -num
    else:
        res = num

    if res > 0x7FFFFFFF or res < -0x80000000:
        return 0
    return res






def get_sign_num(s: str) -> int:
    signs = set(("+", "-"))
    length = len(s)
    i, k = 0, 0
    while i < length and s[i] in signs:
        if s[i] == "-":
            k += 1
        i += 1
    return i, k
def str2int2(s: str) -> int:
    digits = set(map(str, range(10)))
    sign_num, minus_num = get_sign_num(s)
    s = s[sign_num:]
    if not s:
        print("invalid => with only + or -")
        return 0
    if s[0] == "0":
        for i in s[1:]:
            if i != "0":
                print("invalid => 0xx")
                return 0
    for i in s:
        if i not in digits:
            print("invalid => must be 0~9 or + -")
            return 0
    minus = True if minus_num % 2 == 1 else False
    return toint2(s, minus)
def toint2(s: str, minus: bool) -> int:
    length = len(s)
    num = 0
    for i in s:
        num += int(i) * 10 ** (length - 1)
        length -= 1
    if minus:
        num = -num
    if num > 0x7FFFFFFF or num < -0x80000000:
        return 0
    return num



if __name__ == '__main__':
    # s = ""
    # res = str2int(s)
    # print(res)

    print(toint("123", False))

"""

面试题 46：把数字翻译成字符串
题目：给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 "a"，1 翻
译成 "b"，……，11 翻译成 "l"，……，25 翻译成 "z"。一个数字可能有多个翻译。例
如 12258 有 5 种不同的翻译，它们分别是 "bccfi"、"bwfi"、"bczi"、"mcfi" 和
"mzi"。请编程实现一个函数用来计算一个数字有多少种不同的翻译方法。

1 2 2 5 8

1 22 5 8
1 2 25 8
12 2 5 8
12 25 8
"""


def get_translation_count(num: int) -> int:
    """


    Parameters
    -----------

    Returns
    ---------


    Notes
    ------

    """
    if num < 0:
        return 0
    s = str(num)
    lenth = len(s)
    counts = [0] * lenth + [1]
    for i in reversed(range(lenth)):
        count = counts[i+1]
        if i < lenth - 1:
            digit1 = int(s[i])
            digit2 = int(s[i+1])
            converted = digit1 * 10 + digit2
            if 10 <= converted <= 25:
                count += counts[i+2]
        counts[i] = count
    return counts[0]


if __name__ == '__main__':
    num = 426
    res = get_translation_count(num)
    print(res)

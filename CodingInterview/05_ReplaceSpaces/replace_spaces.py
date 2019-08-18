"""
面试题 5：替换空格
题目：请实现一个函数，把字符串中的每个空格替换成 "%20"。例如输入 “We are happy.”，
则输出 “We%20are%20happy.”。
"""

# 这个直接用 python 的 s.replace(" ", "20%") 实在是太没意义了。

def replace(s: str):
    """
    Replace blank to "%20".

    Parameters
    ----------
    s: str
        given string

    Returns
    -------
    out: str
        return string
    """
    if not s:
        return s
    num_blank = 0
    for i in s:
        if i == " ":
            num_blank += 1
    raw_len = len(s)
    new_len = raw_len + num_blank * 2
    res = [''] * new_len
    while new_len >= raw_len > 0:
        if s[raw_len-1] == " ":
            res[new_len-1] = "0"
            res[new_len-2] = "2"
            res[new_len-3] = "%"
            new_len -= 3
        else:
            res[new_len-1] = s[raw_len-1]
            new_len -= 1
        raw_len -= 1
    return "".join(res)

if __name__ == '__main__':
    s = "We are"
    res = replace(s)
    print(res)




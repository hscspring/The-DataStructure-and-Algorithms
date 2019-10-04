"""

面试题 58（一）：翻转单词顺序
题目：输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变。
为简单起见，标点符号和普通字母一样处理。例如输入字符串 "I am a student."，
则输出 "student. a am I"。
"""



def reverse_sentence(s: str) -> str:
    """
    

    Parameters
    -----------

    Returns
    ---------
    out: Reversed words in s.

    Notes
    ------

    """
    reverse = "".join(reversed(s))
    res = []
    splits = reverse.split()
    if not splits:
        return reverse
    for w in splits:
        w = "".join(reversed(w))
        res.append(w)
    return " ".join(res)



def reverse_sentence_easy(s: str) -> str:
    splits = s.split()
    if not splits:
        return s
    return " ".join(reversed(splits))

def reverse_sentence_no_builtin(s: str) -> str:
    begin, end = 0, 1
    rsd_s = reverse(s)
    lens = len(s)
    res = []
    while begin < lens - 1 and end < lens:
        if rsd_s[begin] == " ":
            begin += 1
            end += 1
        elif rsd_s[end] == " ":
            rsd_w = reverse(rsd_s[begin: end])
            res.append(rsd_w)
            begin = end
        else:
            end += 1
    if not res:
        return s
    else:
        res.append(reverse(rsd_s[begin: end+1]))
    return " ".join(res)

def reverse(s: str) -> str:
    res = []
    for i in range(1, len(s)+1):
        res.append(s[-i])
    return "".join(res)


if __name__ == '__main__':
    s = "xyz"
    res = reverse_sentence_easy(s)
    print(res)
    res = reverse_sentence(s)
    print(res)
    
    res = reverse_sentence_no_builtin(s)
    print(res)













    
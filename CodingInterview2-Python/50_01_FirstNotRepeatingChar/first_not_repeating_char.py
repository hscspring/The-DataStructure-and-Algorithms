"""
面试题50（一）：字符串中第一个只出现一次的字符
题目：在字符串中找出第一个只出现一次的字符。如输入"abaccdeff"，则输出
'b'。

"""



def first_not_repeat(s: str) -> str:
    """
    

    Parameters
    -----------

    Returns
    ---------


    Notes
    ------

    """
    if not s:
        return ""
    dct = {}
    for c in s:
        if c in dct:
            dct[c] += 1
        else:
            dct[c] = 1
    for c in s:
        if dct[c] == 1:
            return c
    return ""






if __name__ == '__main__':
    pass













    
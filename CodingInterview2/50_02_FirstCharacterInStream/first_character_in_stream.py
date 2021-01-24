"""
面试题 50（二）：字符流中第一个只出现一次的字符
题目：请实现一个函数用来找出字符流中第一个只出现一次的字符。例如，当从
字符流中只读出前两个字符 "go" 时，第一个只出现一次的字符是 'g'。当从该字
符流中读出前六个字符 "google" 时，第一个只出现一次的字符是 'l'。

"""

dct = {}
lst = []

def first_appear_once(c: str) -> str:
    """
    

    Parameters
    -----------

    Returns
    ---------


    Notes
    ------

    """
    res = ""
    lst.append(c)
    if c in dct:
        dct[c] += 1
    else:
        dct[c] = 1
    
    for c in lst:
        if dct[c] == 1:
            res = c
            break
    return res
    






if __name__ == '__main__':
    while True:
        inputs = input(">>")
        res = first_appear_once(inputs)
        print(res)














    
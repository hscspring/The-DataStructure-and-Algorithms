"""

面试题 58（二）：左旋转字符串
题目：字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。
请定义一个函数实现字符串左旋转操作的功能。比如输入字符串 "abcdefg" 和数
字 2，该函数将返回左旋转 2 位得到的结果 "cdefgab"。

"""



def left_rotate_string(s: str, index: int) -> str:
    """
    

    Parameters
    -----------

    Returns
    ---------

    Notes
    ------

    """
    if not s:
        return s
    left = reverse(s[:index])
    right = reverse(s[index:])
    return reverse(left+right)


def reverse(s: str) -> str:
    res = []
    for i in range(1, len(s)+1):
        res.append(s[-i])
    return "".join(res)


def left_rotate_string_easy(s: str, index: int) -> str:
    if not s:
        return s
    return s[index:] + s[:index]



if __name__ == '__main__':
    s = "abcdefg"
    res = left_rotate_string(s, -7)
    print(res)


    res = left_rotate_string_easy(s, -7)
    print(res)














    
"""
面试题 20：表示数值的字符串
题目：请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。例如，
字符串 “+100”、“5e2”、“-123”、“3.1416” 及 “-1E-16” 都表示数值，但 “12e”、
“1a3.14”、“1.2.3”、“+-5” 及 “12e+5.4” 都不是

"""

z2n = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def is_num(s: str) -> bool:
    """
    Whether a given string is a number.

    Parameters
    -----------
    s: str
        The given string.
    Returns
    ---------
    out: bool
        Whether the string is a number.

    Notes
    ------
    The pattern is:
    [+|-]A[.[B]][[e|E][+|-]C] or .B[[e|E][+|-]C]
    A means integral part
    B means decimal part
    C means exponential part
    """
    if not s:
        return False
    checked, remain = scan_integer(s)

    if not remain:
        # 00001 == False, 00000 == True, 00001.1 == True
        if checked[0] == "0" and checked.count("0") < len(checked):
            return False
        else:
            return True
    
    if remain[0] == ".":
        remain = remain[1:]
        if checked or remain:
            _, remain = scan_unsigned_integer(remain)
            if not remain:
                return True
    if checked and (remain[0] == "e" or remain[0] == "E"):
        remain = remain[1:]
        if remain:
            _, remain = scan_integer(remain)
            if not remain:
                return True
    return False


def scan_integer(s: str):
    """
    Whether the given string is an integer (with sign).
    """
    if s and (s[0] == "+" or s[0] == "-"):
        s = s[1:]
    return scan_unsigned_integer(s)


def scan_unsigned_integer(s: str):
    checked = []
    while s and s[0] in z2n:
        checked.append(s[0])
        s = s[1:]
    return "".join(checked), s

if __name__ == '__main__':
    res = is_num("+.")
    print(res)








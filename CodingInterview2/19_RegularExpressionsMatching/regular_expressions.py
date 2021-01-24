"""
面试题 19：正则表达式匹配
题目：请实现一个函数用来匹配包含 '.' 和 '*' 的正则表达式。模式中的字符 '.'
表示任意一个字符，而 '*' 表示它前面的字符可以出现任意次（含 0 次）。在本题
中，匹配是指字符串的所有字符匹配整个模式。例如，字符串 "aaa" 与模式 "a.a"
和 "ab*ac*a" 匹配，但与 "aa.a" 及 "ab*a" 均不匹配。

"""


def match_dp(string: str, pattern: str) -> bool:
    """
    Map pattern to string.

    Parameters
    -----------
    string: str
        given string.
    pattern: str
        given pattern
    Returns
    ---------
    out: bool
        whether the pattern is match the string.

    Notes
    ------

    """
    T = [[False] * (len(pattern)+1) for _ in range(len(string)+1)]
    T[0][0] = True
    for j in range(len(pattern)):
        if pattern[j] == "*":
            T[0][j+1] = T[0][j-1]
    for i in range(len(string)):
        for j in range(len(pattern)):
            if string[i] == pattern[j] or pattern[j] == ".":
                T[i+1][j+1] = T[i][j]
            elif pattern[j] == "*":
                T[i+1][j+1] = T[i+1][j-1]
                if not T[i+1][j+1]:
                    if pattern[j-1] == "." or pattern[j-1] == string[i]:
                        T[i+1][j+1] = T[i][j+1]
            else:
                # actual is False
                continue
    return T[-1][-1]


def match_recursion(string: str, pattern: str) -> bool:
    if not string and not pattern:
        return True
    if not pattern and string:
        return False

    first_match = string and (string[0] == pattern[0] or pattern[0] == ".")

    if len(pattern) > 1 and pattern[1] == "*":
        if first_match:
            # one time, two times, zero time
            return (match_recursion(string[1:], pattern[2:]) or
                    match_recursion(string[1:], pattern) or
                    match_recursion(string, pattern[2:]))
        else:
            return match_recursion(string, pattern[2:])

    if first_match:
        return match_recursion(string[1:], pattern[1:])

    return False


if __name__ == '__main__':
    res = match_dp("", "")
    print(res)

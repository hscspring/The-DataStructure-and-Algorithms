"""
面试题 48：最长不含重复字符的子字符串
题目：请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子
字符串的长度。假设字符串中只包含从 'a' 到 'z' 的字符。

"""

def find_sub_string_length_dict(s: str) -> int:
    n = len(s)
    hd = {}
    ans,j = 0,0
    for i in range(len(s)):
        if s[i] in hd:
            j = max(hd[s[i]], j)
        ans = max(ans, i-j+1)
        hd[s[i]] = i+1
    return ans

def find_sub_string_length_set(s: str) -> int:
    """
    

    Parameters
    -----------

    Returns
    ---------


    Notes
    ------

    """
    if not s:
        return 0
    i, j, res, n = 0, 0, 0, len(s)
    slide = set()
    while i < n and j < n:
        if s[i] not in slide:
            slide.add(s[i])
            i += 1
            res = max(res, len(slide))
        else:
            slide.remove(s[j])
            j += 1
    return res


def find_sub_string_length_dp1(s: str) -> int:
    if not s:
        return 0
    cur_len, max_len = 0, 0
    abc = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split()
    positions = dict(zip(abc, [-1] * 26))
    for i,c in enumerate(s):
        preindex = positions[c]
        if preindex < 0 or i - preindex > cur_len:
            cur_len += 1
        
        else:
            if cur_len > max_len:
                max_len = cur_len
            cur_len = i - preindex
        
        positions[c] = i
        if cur_len > max_len:
            max_len = cur_len
    return max_len

def find_sub_string_length_dp2(s: str) -> int:
    if not s:
        return 0
    n = len(s)
    dp = [1] + [0] * (n - 1)
    tmp = [s[0]]
    for i in range(1, n):
        if s[i] not in tmp:
            dp[i] = 1 + dp[i-1]
        else:
            # preindex = last_index(tmp, s[i])
            preindex = len(tmp) - tmp[::-1].index(s[i]) - 1
            d = i - preindex
            if d <= dp[i-1]:
                dp[i] = d
            # else:
            #     dp[i] = dp[i-1] + 1
        tmp.append(s[i])
    return max(dp)


def last_index(lst: list, c: str) -> int:
    res = 0
    for i in range(len(lst)):
        if lst[i] == c:
            res = i
    return res



if __name__ == '__main__':
    res = find_sub_string_length_dp2("aaabbbccc")
    print(res)













    
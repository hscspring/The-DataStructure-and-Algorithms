def longestCommonPrefix(strs):
    if len(strs) == 0:
        return ""
    minlen, minid = min([(len(_),i) for i,_ in enumerate(strs)])
    short = strs[minid]
    res = ""
    for i in range(minlen):
        k = 0
        for s in strs:
            if short[i] == s[i]:
                k += 1
                continue
            else:
                break
        if k == len(strs):
            res += short[i]
        else:
            break
    return res


if __name__ == '__main__':
    assert longestCommonPrefix(["flower","flow","flight"]) == "fl"
    assert longestCommonPrefix(["dog","racecar","car"]) == ""
    assert longestCommonPrefix([]) == ""
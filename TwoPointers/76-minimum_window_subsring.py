from collections import Counter


def min_window(s: str, t: str) -> str:
    miss = {}
    for c in  t:
        if c in miss:
            miss[c] += 1
        else:
            miss[c] = 1
    cnt = 0
    lent = len(t)
    lens = len(s)
    l = 0
    head = 0
    d = lens + 1
    for r,c in enumerate(s):
        if c in miss:
            miss[c] -= 1
            if miss[c] >= 0:
                cnt += 1
            while cnt == lent:
                if r - l + 1 < d:
                    head = l
                    d = r - l + 1
                if s[l] in miss:
                    miss[s[l]] += 1
                    if miss[s[l]] > 0:
                        cnt -= 1
                l += 1

    if d > len(s):
        return ""
    else:
        return s[head: head+d]



if __name__ == "__main__":
    lst = [("ADOBECODEBANC", "ABC"), ("bba", "ab"), ("ab", "a")]
    for item in lst:
        s = item[0]
        t = item[1]
        res = min_window(s, t)
        print(res)




def valid_palindrome(s: str) -> bool:
    lens = len(s)
    res = True
    j, k = 0, 0
    for i in range(int(lens/2)):
        if s[i] == s[-1-i-j] or s[i+k] == s[-1-i]:
            continue
        else:
            if (j == 0 and s[i] == s[-1-i-1]) or (k == 0 and s[i+1] == s[-1-i]):
                j += 1
                k += 1
            else:
                return False
    return res

def valid_palindrome2(s: str) -> bool:
    return move(s, "left") or self.move(s, "right")

def move(s: str, direction: str):
    count = 0
    l, r = 0, len(s)-1
    while l < r:
        if s[l] == s[r]:
            l += 1
            r -= 1
        else:
            count += 1
            if count > 1:
                return False
            if direction == "left":
                l += 1
            else:
                r -= 1
    return True

def valid_palindrome4(s: str) -> bool:
    l, r = 0, len(s) - 1
    while l < r:
        if s[l] == s[r]:
            l += 1
            r -= 1
        else:
            return nxt(s, l+1, r) or nxt(s, l, r-1)
    return True

def nxt(s: str, i, j):
    while i < j:
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            return False
    return True


if __name__ == '__main__':
    s = "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"
    res = valid_palindrome4(s)
    print(res)

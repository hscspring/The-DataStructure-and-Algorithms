class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        T = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        T[0][0] = True
        for j in range(len(p)):
            if p[j] == "*":
                T[0][j+1] = T[0][j]
        for i in range(len(s)):
            for j in range(len(p)):
                if s[i] == p[j] or p[j] == "?":
                    T[i+1][j+1] = T[i][j]
                elif p[j] == "*":
                    T[i+1][j+1] = T[i+1][j] or T[i][j+1]
                else:
                    continue
        return T[-1][-1]


if __name__ == '__main__':
    so = Solution()
    s = "aa"
    p = "a"
    assert so.isMatch(s, p) == False
    s = "aa"
    p = "*"
    assert so.isMatch(s, p) == True
    s = "cb"
    p = "?a"
    assert so.isMatch(s, p) == False
    s = "adceb"
    p = "*a*b"
    assert so.isMatch(s, p) == True
    s = "acdcb"
    p = "a*c?b"
    assert so.isMatch(s, p) == False
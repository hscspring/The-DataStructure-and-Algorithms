class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        T = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        T[0][0] = True
        for j in range(len(p)):
            if p[j] == "*":
                T[0][j+1] = T[0][j-1]
        for i in range(len(s)):
            for j in range(len(p)):
                if s[i] == p[j] or p[j] == ".":
                    T[i+1][j+1] = T[i][j]
                elif p[j] == "*":
                    T[i+1][j+1] = T[i+1][j-1]
                    if not T[i+1][j+1]:
                        if p[j-1] == "." or p[j-1] == s[i]:
                            T[i+1][j+1] = T[i][j+1]
                else:
                    continue
        return T[-1][-1]

if __name__ == '__main__':
    so = Solution()
    assert so.isMatch("ab", ".*..c*") == True
    assert so.isMatch("a", ".*..a*") == False
    assert so.isMatch("ab", ".*..") == True
    assert so.isMatch("aa", "a") == False
    assert so.isMatch("aa", "a*") == True
    assert so.isMatch("ab", ".*") == True
    assert so.isMatch("aab", "c*a*b") == True
    assert so.isMatch("mississippi", "mis*is*p*.") == False
    assert so.isMatch("ab", "a.") == True
    assert so.isMatch("aa", "a.") == True
    assert so.isMatch("a", "a.") == False
    assert so.isMatch("axb", "a.b*") == True
    assert so.isMatch("ax", "a.b*") == True
    assert so.isMatch("axc", "a.b*") == False
    assert so.isMatch("ac", "a.*") == True
    assert so.isMatch("abc", "a.*") == True
    assert so.isMatch("ab", "ab.*") == True
    assert so.isMatch("abcde", "ab.*") == True
    assert so.isMatch("ac", "ab.*") == False
    assert so.isMatch("ab", "a.*b") == True
    assert so.isMatch("ab", "a.*b*") == True
    assert so.isMatch("abb", "a.*b*") == True
    assert so.isMatch("aaa", "a*a") == True
    assert so.isMatch("aaa", "ab*ac*a") == True
    assert so.isMatch("aaa", "ab*a*c*a") == True

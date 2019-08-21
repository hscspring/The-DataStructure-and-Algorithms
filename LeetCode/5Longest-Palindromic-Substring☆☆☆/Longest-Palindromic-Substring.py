class Solution2:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        lenps = 0
        res = ""
        for i in range(n):
            j, k = 1, 1
            # For odd number substring
            while i-j >= 0 and i+j < n and s[i-j] == s[i+j]:
                j += 1
            # For even number substring
            while i-(k-1) >= 0 and i+k < n and s[i-k+1] == s[i+k]:
                k += 1
            psj = s[i-j+1: i+j]
            psk = s[i-(k-1)+1: i+(k-1)+1]
            ps = psj if len(psj) > len(psk) else psk
            if len(ps) > lenps:
                res = ps
                lenps = len(ps)
        return res
# the last test case time exceeded
class Solution1:
    def ispalindromic(self, string):
        index = int(len(string)/2)
        res = True
        for i in range(index):
            if string[i] == string[-i-1]:
                continue
            else:
                res = False
                break
        return res
    def longestPalindrome(self, s: str) -> str:
        res = ""
        length = 0
        for i in range(len(s)):
            base = s[i:]
            if len(base) <= length:
                continue
            for i in reversed(range(len(base))):
                subs = base[:i+1]
                if len(subs) <= length:
                    continue
                if self.ispalindromic(subs):
                    res = subs
                    length = len(subs)
        return res


if __name__ == '__main__':
    solution = Solution2()
    string = "babad"
    assert solution.longestPalindrome(string) == "bab"
    string = "abcdcba"
    assert solution.longestPalindrome(string) == "abcdcba"
    string = "abba"
    assert solution.longestPalindrome(string) == "abba"
    string = "aabaa"
    assert solution.longestPalindrome(string) == "aabaa"
    string = "aaaaab"
    assert solution.longestPalindrome(string) == "aaaaa"
    string = "aaaaaab"
    assert solution.longestPalindrome(string) == "aaaaaa"
    string = "baaaaaa"
    assert solution.longestPalindrome(string) == "aaaaaa"
    string = "baaaaa"
    assert solution.longestPalindrome(string) == "aaaaa"
    string = "aaaaaa"
    assert solution.longestPalindrome(string) == "aaaaaa"
    string = "aaaaa"
    assert solution.longestPalindrome(string) == "aaaaa"
    string = "cbbd"
    assert solution.longestPalindrome(string) == "bb"
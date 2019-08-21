class Solution:
    def validPalindrome(self, s: str) -> bool:
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


if __name__ == '__main__':
    so = Solution()
    assert so.validPalindrome("aba") == True
    assert so.validPalindrome("abca") == True
    assert so.validPalindrome("abcd") == False
    assert so.validPalindrome("abc") == False
    assert so.validPalindrome("eedede") == True
    assert so.validPalindrome("ebcbbececabbacecbbcbe") == True
    assert so.validPalindrome("dmaadedaeeddeeadedafad") == False
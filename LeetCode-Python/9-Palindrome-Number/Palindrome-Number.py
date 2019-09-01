class Solution:
    def isPalindrome(self, x: int) -> bool:
        res = True
        s = str(x)
        for i in range(int(len(s)/2)):
            if s[i] == s[-1-i]:
                continue
            else:
                res = False
                break
        return res

if __name__ == '__main__':
    so = Solution()
    assert so.isPalindrome(1232321) == True
    assert so.isPalindrome(121) == True
    assert so.isPalindrome(1) == True
    assert so.isPalindrome(11) == True
    assert so.isPalindrome(-121) == False
    assert so.isPalindrome(10) == False
class Solution:
    def remove_nonalph(self, s):
        letters = 'abcdefghijklmnopqrstuvwxyz0123456789'
        s = s.lower()
        res = []
        for l in s:
            if l in letters:
                res.append(l)
        return "".join(res)
    def isPalindrome(self, s: str) -> bool:
        res = True
        news = self.remove_nonalph(s)
        lens = len(news)
        for i in range(int(lens/2)):
            if news[i] == news[-1-i]:
                continue
            else:
                res = False
                break
        return res

if __name__ == '__main__':
    so = Solution()
    assert so.isPalindrome("A man, a plan, a canal: Panama") == True
    assert so.isPalindrome("race a car") == False
    assert so.isPalindrome("") == True
    assert so.isPalindrome("*") == True
    assert so.isPalindrome("&*(") == True
    assert so.isPalindrome("0P") == False
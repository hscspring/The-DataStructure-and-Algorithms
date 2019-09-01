class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romanDict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        res = 0
        i = 0
        while i < len(s) - 1:
            if romanDict[s[i+1]] > romanDict[s[i]]:
                res += romanDict[s[i+1]] - romanDict[s[i]]
                i += 2
            else:
                res += romanDict[s[i]]
                i += 1
        if i < len(s):
            res += romanDict[s[i]]
        return res

if __name__ == '__main__':
    so = Solution()
    assert so.romanToInt("III") == 3
    assert so.romanToInt("IV") == 4
    assert so.romanToInt("IX") == 9
    assert so.romanToInt("LVIII") == 58
    assert so.romanToInt("MCMXCIV") == 1994
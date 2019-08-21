class Solution(object):
    def intToRoman(self, num):
        """
        Int ot Roman.

        Parameters
        -----------
        num: int
            Input number
        Returns
        -------
        Roman string equals to the input num.
        """
        romanDict = {
            0: '',
            1: 'I', 
            5: 'V', 
            10: 'X', 
            50: 'L', 
            100: 'C', 
            500: 'D', 
            1000: 'M'}
        roman = ""
        snum = str(num)
        lens = len(snum)
        for i in range(len(snum)):
            n = int(snum[i])
            loc = 10**(lens-i-1)
            if n == 4 or n == 9:
                roman += romanDict[loc] + romanDict[(n+1) * loc]
            else:
                if n > 5:
                    roman += romanDict[5 * loc] + (n-5) * romanDict[loc]
                elif 1 < n < 5:
                    roman += n * romanDict[loc]
                else:
                    roman += romanDict[n * loc]
        return roman

if __name__ == '__main__':
    so = Solution()
    assert so.intToRoman(3) == "III"
    assert so.intToRoman(4) == "IV"
    assert so.intToRoman(9) == "IX"
    assert so.intToRoman(58) == "LVIII"
    assert so.intToRoman(1994) == "MCMXCIV"
    assert so.intToRoman(85) == "LXXXV"



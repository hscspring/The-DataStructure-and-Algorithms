class Solution:
    def remove_frontspace(self, s):
        i = 0
        while i < len(s) and s[i] == " ":
            i = i + 1
        return s[i:]
    def s2num(self, s):
        news = self.remove_frontspace(s)
        if news == "":
            return 0
        begin = news[0]
        if begin == "-" or begin == "+":
            res = begin
        else:
            try:
                int(begin)
                res = begin
            except ValueError as e:
                return 0
        for i in news[1:]:
            try:
                int(i)
            except ValueError as e:
                break
            res += i
        if res == "" or res == "-" or res == "+":
            num = 0
        else:
            num = int(res)
        return num
    def myAtoi(self, s: str) -> int:
        num = self.s2num(s)
        minn = -(2**31)
        maxn = 2**31-1
        if num < minn:
            num = minn
        elif num > maxn:
            num = maxn
        return num

if __name__ == '__main__':
    solution = Solution()
    assert solution.myAtoi("  +0  123") == 0
    assert solution.myAtoi("+") == 0
    assert solution.myAtoi("-") == 0
    assert solution.myAtoi("-120") == -120
    assert solution.myAtoi("-1+0") == -1
    assert solution.myAtoi("1-+0") == 1
    assert solution.myAtoi("0+1") == 0
    assert solution.myAtoi("1+0") == 1
    assert solution.myAtoi("1-0") == 1
    assert solution.myAtoi("0-1") == 0
    assert solution.myAtoi("4a2") == 4
    assert solution.myAtoi("words and 987") == 0
    assert solution.myAtoi("4193 with words") == 4193
    assert solution.myAtoi("   -42") == -42
    assert solution.myAtoi("42") == 42
    assert solution.myAtoi("") == 0
    assert solution.myAtoi(" ") == 0
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l = 0
        r = int(math.sqrt(c))
        while (l <= r):
            val = l * l + r * r
            if val == c:
                return True
            elif val < c:
                l += 1
            else:
                r -= 1
        return False

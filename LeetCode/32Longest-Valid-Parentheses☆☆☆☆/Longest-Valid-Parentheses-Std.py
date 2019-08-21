# Approach 2
# This method is really awesome.
def longestValidParentheses(s):
    maxans = 0
    dp = [0 for _ in range(len(s))]
    for i in range(1, len(s)):
        if s[i] == ')':
            if s[i-1] == '(':
                dp[i] = 2 + dp[i-2] if i >= 2 else 2
            elif i-dp[i-1] > 0 and s[i-dp[i-1]-1] == '(':
                dp[i] = dp[i-1] + 2+dp[i-dp[i-1]-2] if (i-dp[i-1]) >= 2 else 2
            maxans = max(maxans, dp[i])
    return maxans

# Approach 4
class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        l,r = 0,0
        max_ = 0
        for i in range(len(s)):
            if s[i] == '(':
                l +=1
            else:
                r +=1
            if l == r:
                max_ = max(max_, 2 * r)
            else:
                if r >= l:
                    l = r = 0
        l,r = 0,0
        for i in range(len(s)-1,-1,-1):
            if s[i] == '(':
                l += 1
            else:
                r += 1
            if l == r:
                max_ = max(max_, 2 * l)
            else:
                if l >= r:
                    l = r = 0
        return max_
"""
A sliding window is an abstract concept commonly used in array/string problems. 
A window is a range of elements in the array/string 
which usually defined by the start and end indices, i.e. [i, j)[i,j) (left-closed, right-open). 
A sliding window is a window "slides" its two boundaries to the certain direction.

"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        hs = set()
        ans, i, j = 0, 0, 0
        while i < n and j < n:
            if s[j] not in hs:
                hs.add(s[j])
                j += 1
                ans = max(ans, j-i)
            else:
                hs.remove(s[i])
                i += 1
        return ans

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        hd = {}
        ans,j = 0,0
        for i in range(len(s)):
            if s[i] in hd:
                j = max(hd[s[i]], j)
            ans = max(ans, i-j+1)
            hd[s[i]] = i+1
        return ans
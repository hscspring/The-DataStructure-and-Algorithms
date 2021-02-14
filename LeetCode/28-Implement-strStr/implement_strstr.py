class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                if haystack[i:i+len(needle)] == needle:
                    return i
        return -1





so = Solution()

assert so.strStr("hello", "ll") == 2
assert so.strStr("hellollo", "ll") == 2
assert so.strStr("aaaaa", "bba") == -1
assert so.strStr("", "") == 0
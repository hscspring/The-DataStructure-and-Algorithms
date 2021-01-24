class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        init_len = self.get_len(s)
        if len(set(s)) == init_len:
            return init_len
        res = [init_len]
        for i in range(1, len(s)):
            subs = s[i:]
            if len(subs) < max(res):
                break
            check_s = subs[:init_len]
            if len(set(check_s)) < init_len:
                continue
            sublen = self.get_len(subs)
            res.append(sublen)
        return (max(res))
    def get_len(self, subs: str) -> int:
        past = []
        length = []
        for w in subs:
            if w not in past:
                past.append(w)
            else:
                length.append(len(past))
                past = []
                past.append(w)
        length.append(len(past))
        return (max(length))



if __name__ == '__main__':
    solution = Solution()
    assert solution.lengthOfLongestSubstring("") == 0
    assert solution.lengthOfLongestSubstring("a") == 1
    assert solution.lengthOfLongestSubstring(" ") == 1
    assert solution.lengthOfLongestSubstring("bbbb") == 1
    assert solution.lengthOfLongestSubstring("abcabcbb") == 3
    assert solution.lengthOfLongestSubstring("pwwkew") == 3
    assert solution.lengthOfLongestSubstring("wpwkwe") == 3
    assert solution.lengthOfLongestSubstring("dvdf") == 3
    assert solution.lengthOfLongestSubstring("anviaj") == 5
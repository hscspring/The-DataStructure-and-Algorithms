from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        res = []
        base_len = len(words[0])
        for candi in self.words2str(words):
            tmp = self.get_matched_indexes(s, candi, base_len)
            res.extend(tmp)
        return res


    def get_matched_indexes(self, haystack: str, needle: str, base_len: int):
        if not needle:
            return []
        length = len(needle)
        res = []
        i = 0
        while i < len(haystack) - length + 1:
            if haystack[i] == needle[0] and haystack[i:i+length] == needle:
                res.append(i)
            i += 1
        return res


    def words2str(self, words: list):
        res = set()
        def func(prefix: list, suffix: list):
            if not suffix:
                line = "".join(prefix)
                res.add(line)
            for i in range(len(suffix)):
                func(prefix + [suffix[i]], suffix[:i] + suffix[i+1:])
        func([], words)
        return res


so = Solution()

s = "barfoothefoobarman"
words = ["foo","bar"]
s = "barfoofoobarthefoobarman"
words = ["bar","foo","the"]
# s = "wordgoodgoodgoodbestword"
# words = ["word","good","best","good"]

res = so.findSubstring(s, words)
print(res)
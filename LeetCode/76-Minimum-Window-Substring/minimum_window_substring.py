from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        global_t = [""] * 100000
        local_s = []
        ct = Counter(t)
        for i in s:
            local_s.append(i)
            while self.satisfy(local_s, ct):
                if len(local_s) <= len(global_t):
                    global_t = "".join(local_s)
                local_s.pop(0)
        if type(global_t) == list:
            return ""
        return global_t

    def satisfy(self, ls: list, ct: dict):
        lsct = Counter(ls)
        for k, v in ct.items():
            if lsct.get(k, 0) < v:
                return False
        return True

so = Solution()
s = "ADOBECODEBANC"
t = "ABC"

res = so.minWindow(s, t)
print(res)

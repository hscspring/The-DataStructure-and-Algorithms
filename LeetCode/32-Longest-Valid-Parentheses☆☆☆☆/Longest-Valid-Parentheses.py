# It is wrong.
# It contains non-continuous ()

def longestValidParentheses(s: str) -> int:
    n = 0
    while len(s) > 1:
        remain = []
        remain_id = []
        use = []
        for i in range(len(s)-1):
            if s[i] == "(" and s[i+1] == ")":
                n += 1
                use.append(i)
                use.append(i+1)
        for i in range(len(s)):
            if i in use:
                continue
            remain_id.append(i)
            remain.append(s[i])
        s = "".join(remain)
        if len(set(s)) == 1 or (s == ")("):
            break
    return n * 2


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        use_ids, res = [], []
        remain_ids = list(range(len(s)))
        prelens, n = 0, 0
        while prelens != len(s):
            prelens = len(s)
            remain, use_inner, use = [], [], []
            for i in range(len(s)-1):
                if s[i] == "(" and s[i+1] == ")":
                    use_inner.extend([i, i+1])
                    use.extend(remain_ids[i:i+2])
            use_ids.extend(use)
            for ele in use:
                remain_ids.remove(ele)
            for i in range(len(s)):
                if i in use_inner:
                    continue
                remain.append(s[i])
            s = "".join(remain)
        if len(use_ids) >= 2:
            ids = sorted(use_ids)
            for k in range(len(ids)-1):
                if ids[k+1] - ids[k] == 1:
                    n += 1
                else:
                    res.append(n+1)
                    n = 0
            res.append(n+1)
            n = max(res)
        return n

if __name__ == '__main__':
    so = Solution()
    assert so.longestValidParentheses("(()") == 2
    assert so.longestValidParentheses(")()())") == 4
    assert so.longestValidParentheses("()") == 2
    assert so.longestValidParentheses("((") == 0
    assert so.longestValidParentheses(")(") == 0
    assert so.longestValidParentheses("(") == 0
    assert so.longestValidParentheses("()(())") == 6
    assert so.longestValidParentheses("()(()") == 2
    assert so.longestValidParentheses("((()))())") == 8
    assert so.longestValidParentheses(")(())))(())())") == 6
    assert so.longestValidParentheses("))))())()()(()") == 4




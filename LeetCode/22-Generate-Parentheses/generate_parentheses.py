class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        res = {"()"}
        for i in range(n-1):
            tmp = set()
            for item in res:
                for i in range(len(item)+1):
                    new = item[:i] + "()" + item[i:]
                    tmp.add(new)
            res = tmp
        return list(res)
    
    def generateParenthesis2(self, n):
        def generate(A = []):
            if len(A) == 2*n:
                if valid(A):
                    ans.append("".join(A))
            else:
                A.append('(')
                generate(A)
                A.pop()
                A.append(')')
                generate(A)
                A.pop()

        def valid(A):
            bal = 0
            for c in A:
                if c == '(': bal += 1
                else: bal -= 1
                if bal < 0: return False
            return bal == 0

        ans = []
        generate()
        return ans

    def generateParenthesis3(self, N):
        ans = []
        def backtrack(S = '', left = 0, right = 0):
            if len(S) == 2 * N:
                ans.append(S)
                return
            if left < N:
                backtrack(S+'(', left+1, right)
            if right < left:
                backtrack(S+')', left, right+1)

        backtrack()
        return ans

    def generateParenthesis4(self, N):
        if N == 0: return ['']
        ans = []
        for c in xrange(N):
            for left in self.generateParenthesis4(c):
                for right in self.generateParenthesis4(N-1-c):
                    ans.append('({}){}'.format(left, right))
        return ans
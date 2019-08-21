class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        pnDict = {
        '2' : ['a', 'b', 'c'],
        '3' : ['d', 'e', 'f'],
        '4' : ['g', 'h', 'i'],
        '5' : ['j', 'k', 'l'],
        '6' : ['m', 'n', 'o'],
        '7' : ['p', 'q', 'r', 's'],
        '8' : ['t', 'u', 'v'],
        '9' : ['w', 'x', 'y', 'z']
        }
        res = []
        f = ['']
        lenr = 1
        for i in range(len(digits)):
            tmp = []
            curr = pnDict[digits[i]]
            lenr *= len(curr)
            for ele in f:
                tmp.extend([ele+w for w in curr])
            f = tmp
            res.extend(tmp)
        return res[-lenr:]

if __name__ == '__main__':
    so = Solution()
    assert so.letterCombinations("23") == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    assert so.letterCombinations("234") == ["adg","adh","adi","aeg","aeh","aei","afg","afh","afi",
                                         "bdg","bdh","bdi","beg","beh","bei","bfg","bfh","bfi",
                                         "cdg","cdh","cdi","ceg","ceh","cei","cfg","cfh","cfi"]
    assert so.letterCombinations("27") == ["ap","aq","ar","as","bp","bq","br","bs","cp","cq","cr","cs"]
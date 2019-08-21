class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        res = 0
        dct = {}
        for a in A:
            for b in B :
                if a + b in dct :
                    dct[a+b] += 1
                else :
                    dct[a+b] = 1
        for c in C :
            for d in D :
                if -c-d in dct:
                    res += dct[-c-d]
        return res

# Naive 
class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        res = 0
        for a in A:
            for b in B:
                for c in C:
                    for d in D:
                        if a+b+c+d == 0:
                            res += 1
        return res

def fourSumCount1(A, B, C, D):
    AB = []
    for a in A:
        for b in B:
            AB.append(a+b)
    CD = []
    for c in C:
        for d in D:
            CD.append(c+d)
    res = 0
    for ab in AB:
        for cd in CD:
            if ab + cd == 0:
                res += 1
    return res

def fourSumCount2(A, B, C, D):
    AB = []
    for a in A:
        for b in B:
            AB.append(a+b)
    ABC = []
    for ab in AB:
        for c in C:
            ABC.append(ab+c)
    ABCD = []
    for abc in ABC:
        for d in D:
            ABCD.append(abc+d)
    return ABCD.count(0)




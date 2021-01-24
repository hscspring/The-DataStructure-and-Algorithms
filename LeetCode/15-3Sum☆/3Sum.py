class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        sort = sorted(nums)
        res = []
        for i in range(len(sort) - 2):
            if i > 0 and sort[i] == sort[i-1]:
                continue
            l, r = i+1, len(sort) - 1
            while l < r:
                if sort[i] + sort[l] + sort[r] < 0:
                    l += 1
                elif sort[i] + sort[l] + sort[r] > 0:
                    r -= 1
                else:
                    res.append([sort[i], sort[l], sort[r]])
                    while l < r and sort[l] == sort[l+1]:
                        l += 1
                    while l < r and sort[r] == sort[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
        return res

# lazy approach
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                for k in range(j, len(nums)):
                    if i == j or i == k or j == k:
                        continue
                    if nums[i] + nums[j] + nums[k] == 0:
                        item = sorted((nums[i], nums[j], nums[k]))
                        if item in res:
                            continue
                        res.append(item)
        return res

# O(N*N)
def threeSum1(nums):
    if len(nums) < 3:
        res = []
    zeros, negs, poss = [], [], []
    for i in range(len(nums)):
        item = nums[i]
        if item == 0:
            zeros.append(item)
        elif item > 0:
            poss.append(item)
        else:
            negs.append(item)
    res = []
    if len(zeros) > 0:
        for i in range(len(negs)):
            if -negs[i] in poss:
                item = [negs[i], 0, -negs[i]]
                if item not in res:
                    res.append(item)
        if len(zeros) > 2:
            res.append([0, 0, 0])
    for i in range(len(negs)):
        for j in range(len(poss)):
            tmp = -(negs[i] + poss[j])
            if tmp in negs[0:i] + negs[i+1:]:
                big, small = (negs[i], tmp) if negs[i] > tmp else (tmp, negs[i])
                item = [small, big, poss[j]]
            elif tmp in poss[0:j] + poss[j+1:]:
                big, small = (poss[j], tmp) if poss[j] > tmp else (tmp, poss[j])
                item = [negs[i], small, big]
            else:
                continue
            if item not in res:
                res.append(item)
    return res

# BE careful to use python `ele in list`, it's O(n)
def threeSum2(nums):
    if len(nums) < 3:
        res = []
    zeros, negs, poss = [], [], []
    for i in range(len(nums)):
        item = nums[i]
        if item == 0:
            zeros.append(item)
        elif item > 0:
            poss.append(item)
        else:
            negs.append(item)
    res = []
    if len(zeros) > 0:
        for i in range(len(negs)):
            if -negs[i] in poss:
                item = [negs[i], 0, -negs[i]]
                if item not in res:
                    res.append(item)
        if len(zeros) > 2:
            res.append([0, 0, 0])

    sorted_negs = sorted(negs)
    sorted_poss = sorted(poss)

    for i in range(len(sorted_negs)):
        if i > 0 and sorted_negs[i] == sorted_negs[i-1]:
            continue
        l, r = 0, len(sorted_poss) - 1
        while l < r:
            if sorted_negs[i] + sorted_poss[l] + sorted_poss[r] == 0:
                item = [sorted_negs[i], sorted_poss[l], sorted_poss[r]]
                if item not in res:
                    res.append(item)
                l += 1
                r -= 1
            elif sorted_negs[i] + sorted_poss[l] + sorted_poss[r] < 0:
                l += 1
            else:
                r -= 1

    for i in range(len(sorted_poss)):
        if i > 0 and sorted_poss[i] == sorted_poss[i-1]:
            continue
        l, r = 0, len(sorted_negs) - 1
        while l < r:
            if sorted_poss[i] + sorted_negs[l] + sorted_negs[r] == 0:
                item = [sorted_negs[l], sorted_negs[r], sorted_poss[i]]
                if item not in res:
                    res.append(item)
                l += 1
                r -= 1
            elif sorted_poss[i] + sorted_negs[l] + sorted_negs[r] < 0:
                l += 1
            else:
                r -= 1
    return res

def threeNums3(nums):
    if len(nums) < 3:
        res = []
    zeros, negs, poss = [], [], []
    for i in range(len(nums)):
        item = nums[i]
        if item == 0:
            zeros.append(item)
        elif item > 0:
            poss.append(item)
        else:
            negs.append(item)
    res = []
    if len(zeros) > 0:
        for i in range(len(negs)):
            if -negs[i] in poss:
                item = [negs[i], 0, -negs[i]]
                if item not in res:
                    res.append(item)
        if len(zeros) > 2:
            res.append([0, 0, 0])

    sorted_negs = sorted(negs)
    sorted_poss = sorted(poss)

    for i in range(len(sorted_negs)):
        if i > 0 and sorted_negs[i] == sorted_negs[i-1]:
            continue
        l, r = 0, len(sorted_poss) - 1
        while l < r:
            if sorted_negs[i] + sorted_poss[l] + sorted_poss[r] == 0:
                item = [sorted_negs[i], sorted_poss[l], sorted_poss[r]]
                res.append(item)
                while l < r and sorted_poss[l] == sorted_poss[l+1]:
                    l += 1
                while l < r and sorted_poss[r] == sorted_poss[r-1]:
                    r -= 1
                l += 1
                r -= 1
            elif sorted_negs[i] + sorted_poss[l] + sorted_poss[r] < 0:
                l += 1
            else:
                r -= 1

    for i in range(len(sorted_poss)):
        if i > 0 and sorted_poss[i] == sorted_poss[i-1]:
            continue
        l, r = 0, len(sorted_negs) - 1
        while l < r:
            if sorted_poss[i] + sorted_negs[l] + sorted_negs[r] == 0:
                item = [sorted_negs[l], sorted_negs[r], sorted_poss[i]]
                res.append(item)
                while l < r and sorted_negs[l] == sorted_negs[l+1]:
                    l += 1
                while l < r and sorted_negs[r] == sorted_negs[r-1]:
                    r -= 1
                l += 1
                r -= 1
            elif sorted_poss[i] + sorted_negs[l] + sorted_negs[r] < 0:
                l += 1
            else:
                r -= 1
    return res

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) < 4:
            return []
        if len(nums) == 4 and sum(nums) == target:
            return [nums]
        reset = []
        for i in range(len(nums)):
            subtar = target-nums[i]
            newnums = nums[:i] + nums[i+1: ]
            for item in threeSum(newnums, subtar):
                item.append(nums[i])
                if sum(item) == target:
                    reset.append(sorted(item))
        res = []
        sort = [[]] + sorted(reset)
        for i in range(1, len(sort)):
            if sort[i-1] != sort[i]:
                res.append(sort[i])
        return res

def threeSum(nums, target):
    sort = sorted(nums)
    res = []
    for i in range(len(sort) - 2):
        if i > 0 and sort[i] == sort[i-1]:
            continue
        l, r = i+1, len(sort) - 1
        while l < r:
            if sort[i] + sort[l] + sort[r] < target:
                l += 1
            elif sort[i] + sort[l] + sort[r] > target:
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


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        sort = sorted(nums)
        res, tmp = [], []
        for i in range(len(sort) - 3):
            for j in range(i+1, len(sort) - 2):
                if i > 0 and sort[i] == sort[i-1] and sort[j] == sort[j-1]:
                    continue
                l, r = j+1, len(sort) - 1
                while l < r:
                    if sort[i] + sort[j] + sort[l] + sort[r] < target:
                        l += 1
                    elif sort[i] + sort[j] + sort[l] + sort[r] > target:
                        r -= 1
                    else:
                        tmp.append([sort[i], sort[j], sort[l], sort[r]])
                        while l < r and sort[l] == sort[l+1]:
                            l += 1
                        while l < r and sort[r] == sort[r-1]:
                            r -= 1
                        l += 1
                        r -= 1
        sort = [[]] + sorted(tmp)
        for i in range(1, len(sort)):
            if sort[i-1] != sort[i]:
                res.append(sort[i])
        return res








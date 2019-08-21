class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res = sum(nums[:3])
        gap = abs(res - target)
        sort = sorted(nums)
        flag = 0
        for i in range(len(sort) - 2):
            l, r = i+1, len(sort) - 1
            while l < r:
                add = sort[i] + sort[l] + sort[r]
                newgap = abs(add - target)
                if newgap > gap:
                    if add < target:
                        l += 1
                    elif add > target:
                        r -= 1
                    else:
                        l += 1
                        r -= 1
                else:
                    gap = newgap
                    res = add
                    if add < target:
                        l += 1
                    elif add > target:
                        r -= 1
                    else:
                        flag = 0
                        break
            if flag:
                break
        return res



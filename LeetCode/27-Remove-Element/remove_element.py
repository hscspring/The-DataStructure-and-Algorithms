from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        flag = False
        i = len(nums) - 1
        for j in range(len(nums)):
            if nums[j] == val:
                while i > j and nums[i] == val:
                    i -= 1
                nums[j] = nums[i]
                nums[i] = val
                flag = True
        if not flag:
            i = i + 1
        return i

    def removeElement2(self, nums: List[int], val: int) -> int:
        i, j = 0, len(nums) - 1
        while i < j:
            if nums[i] == val:
                nums[i] = nums[j]
                j -= 1
            else:
                i += 1
        return j

    def removeElement3(self, nums: List[int], val: int) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i

so = Solution()


lst = [0,1,2,2,3,0,4,2]
val = 2

res = so.removeElement(lst, val)
print(res)
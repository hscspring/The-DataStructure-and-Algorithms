class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        start = 0
        global_max = sum(nums[:k])
        curr_sum = global_max
        for i in range(1, len(nums) - k + 1):
            curr_sum = curr_sum - nums[i-1] + nums[i-1+k]
            if curr_sum > global_max:
                global_max = curr_sum
        return global_max / k
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        global_len = 1e5
        local_sum = 0
        k = 0
        for i in range(len(nums)):
            local_sum += nums[i]
            while local_sum >= s:
                global_len = min(global_len, i - k + 1)
                local_sum -= nums[k]
                k += 1
        if global_len == 1e5:
            return 0
        return global_len
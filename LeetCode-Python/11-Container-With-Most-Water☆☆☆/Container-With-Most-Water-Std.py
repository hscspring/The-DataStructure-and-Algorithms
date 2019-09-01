"""
The Explain: https://leetcode.com/problems/container-with-most-water/discuss/6100/Simple-and-clear-proofexplanation
"""


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxarea, l = 0, 0
        r = len(height) - 1
        while l < r:
            maxarea = max(maxarea, min(height[l], height[r]) * (r - l))
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return maxarea


if __name__ == '__main__':
    so = Solution()
    assert so.maxArea([1,8,6,2,5,4,8,3,7]) == 49
    assert so.maxArea([1,1]) == 1
    assert so.maxArea([1,2,1]) == 2
    assert so.maxArea([2,3,4,5,18,17,6]) == 17
    assert so.maxArea([1,2,3,4,5,6,7,8,9,10]) == 25
    assert so.maxArea([8,10,14,0,13,10,9,9,11,11]) == 80
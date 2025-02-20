"""
给定一个非负整数组成的数组arr，每个数表示从当前位置**最多**可以前进的步数。
问题：从数组的第0位出发，是否可以达到最后一位？

例1：输入arr=[4,1,1,2,0,3]，返回True。原因：从arr[0]出发，可以选择前进3步到达arr[3]，再选择前进2步可到达最后一位
例2：输入arr=[3,2,1,0,1,2]，返回False。原因：从arr[0]出发，无论如何选择，最多达到arr[3]，无法到达最后一位
"""


def solution(arr):
    mi = 0
    n = len(arr)
    for i in range(n):
        if i > mi:
            return False
        mi = max(mi, i + arr[i])
        if mi >= n - 1:
            return True
    return False


assert solution([4, 1, 1, 2, 0, 3]) == True
assert solution([3, 2, 1, 0, 1, 2]) == False
assert solution([2, 3, 1, 1, 4]) == True
assert solution([3, 2, 1, 0, 4]) == False

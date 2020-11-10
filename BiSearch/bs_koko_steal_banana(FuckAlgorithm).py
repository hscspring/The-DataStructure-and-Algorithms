# N 堆香蕉，第 i 堆有 piles[i] 根香蕉，假设吃香蕉速度为 K根/小时，求 H 小时内吃完所有香蕉的最小速度。
# 每个小时选择一堆，吃掉 K 根，如果这堆香蕉少于 K 根，就吃掉所有香蕉并不再多吃。

"""
Input: piles = [3,6,7,11], H = 8
Output: 4

Input: piles = [30, 11, 23, 4, 20], H = 5
Output: 30

"""


def brute_force(piles: list, hour: int):
    max_num = max(piles)
    for i in range(1, max_num+1):
        time_cost = can_eat_up(i, hour, piles)
        if time_cost:
            return i
    return max_num


def can_eat_up(speed: int, hour: int, piles: list):
    result = 0
    for i in piles:
        result += i // speed + 1
    return hour >= result


def bisearch(piles: list, hour: int):
    l, r = 0, len(piles)
    while l < r:
        mid = (l + r) // 2
        time_cost = can_eat_up(mid, hour, piles)
        if time_cost:
            r = mid
        else:
            l = mid + 1
    return l


for func in (brute_force, bisearch):
    assert brute_force([3,6,7,11], 8) == 4
    assert brute_force([30, 11, 23, 4, 20], 5) == 30
    assert brute_force([10], 3) == 4
    assert brute_force([10], 1) == 10

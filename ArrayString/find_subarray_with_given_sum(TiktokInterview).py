# -*- coding: utf-8 -*-

"""
Given an unsorted array of integers, find a subarray which adds to a given number.
If there are more than one subarrays with the sum as the given number, print any of them.
"""


def find_subarray_with_given_sum1(lst: list, target: int) -> tuple:
    slide = []
    for i, v in enumerate(lst):
        slide.append(v)
        while sum(slide) > target and slide:
            slide.pop(0)
        if sum(slide) == target:
            return (i-len(slide)+1, i)
    return (-1, -1)


def find_subarray_with_given_sum2(lst: list, target: int) -> tuple:
    """
    当前累计和与之前累计和相减后正好就是 之前位置到当前位置的累计和。
    """
    dct = {}
    curr_sum = 0
    for i, v in enumerate(lst):
        curr_sum += v
        dct[curr_sum] = i
        if curr_sum - target in dct:
            return (dct.get(curr_sum - target)+1, i)
    return (-1, -1)


def find_subarray_with_given_sum3(lst: list, target: int) -> tuple:
    start = 0
    curr_sum = 0
    for i, v in enumerate(lst):
        curr_sum += v
        while curr_sum > target and start < i-1:
            curr_sum -= lst[start]
            start += 1
        if curr_sum == target:
            return (start, i)
    return (-1, -1)


lists = [
    ([1, 4, 20, 3, 10, 5], 33),
    ([10, 2, -2, -20, 10], -10),
    ([-10, 0, 2, -2, -20, 10], 20),
    ([1, 4, 0, 0, 3, 10, 5], 7),
    ([1, 4], 0)
]

for lst, target in lists:
    for func in [
        find_subarray_with_given_sum1,
        find_subarray_with_given_sum2,
        find_subarray_with_given_sum3
    ]:
        res = func(lst, target)
        print(res)
        if res[0] != -1:
            assert sum(lst[res[0]: res[1]+1]) == target
    print("======")

# -*- coding: utf-8 -*-
import math

def get_max_subarray_loc_sum(lst: list) -> (int, int, int):
    best, sum = -1e5, 0
    for i in lst:
        sum = max(i, sum+i)
        best = max(best, sum)
    return best

def maxSubArraySum(a): 
       
    max_so_far = -1e5 - 1
    max_ending_here = 0

    s = 0
    e = 0
       
    for i in range(0, len(a)): 
        max_ending_here = max_ending_here + a[i] 
        if (max_so_far < max_ending_here): 
            max_so_far = max_ending_here 
            e += 1
  
        if max_ending_here < 0: 
            max_ending_here = 0
            s = i + 1

    return s, e #, max_so_far 


def maxSubArraySum(arr):
    # https://www.collegestash.com/kadanes-algorithm-maximum-sum-subarray-indices-handles-negatives/
    # https://medium.com/@rsinghal757/kadanes-algorithm-dynamic-programming-how-and-why-does-it-work-3fd8849ed73d
    global_max, curr_max = -math.inf, -math.inf
    start, end, k = 0, 0, 0
    for i,v in enumerate(arr):
        curr_max +== v
        if curr_max < v:
            curr_max = v
            k = i
        if curr_max > global_max:
            global_max = curr_max
            start = k
            end = i
    return start, end, global_max

lst1 = [-1, 2, 4, -3, 5, 2, -5, 2]
lst2 = [-1, -5, -4]
lst3 = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]
lst5 = [0, 0, 0, 0, 1, -1, 2, 0, 0, 0]
lst6 = [-10, -2, 1, 2, 3, 4, -5, -23, 3, 7, -21]
lsts = [lst1, lst2, lst3, lst5, lst6]
for lst in lsts:
    # print(get_max_subarray_loc_sum(lst))
    print(maxSubArraySum(lst))




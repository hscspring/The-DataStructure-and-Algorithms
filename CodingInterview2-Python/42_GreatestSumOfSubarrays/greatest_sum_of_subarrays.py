"""
面试题 42：连续子数组的最大和
题目：输入一个整型数组，数组里有正数也有负数。数组中一个或连续的多个整
数组成一个子数组。求所有子数组的和的最大值。要求时间复杂度为 O (n)。


"""



def find_greatest_sum_of_sub_array(lst: list) -> int:
    """
    

    Parameters
    -----------

    Returns
    ---------


    Notes
    ------

    """
    if not lst:
        return 0
    curr, res = 0, lst[0]
    for i in lst:
        if curr <= 0:
            curr = i
        else:
            curr += i
        if curr >= res:
            res = curr
    return res


def find_greatest_sum_of_sub_array_dp(lst: list) -> int:
    if not lst:
        return 0
    dp = [lst[0]] + [0] * (len(lst)-1)
    res = dp[0]
    for i in range(1, len(lst)):
        if dp[i-1] <= 0:
            dp[i] = lst[i]
        else:
            dp[i] = dp[i-1] + lst[i]
        # res = max(dp[i], res)
    return max(dp)





if __name__ == '__main__':
    lst = [-2, -8, -1, -5, -9]
    # lst = [1, -2, 3, 10, -4, 7, 2, -5]
    res = find_greatest_sum_of_sub_array_dp(lst)
    print(res)













    
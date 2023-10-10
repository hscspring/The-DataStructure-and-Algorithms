"""
给出一个整数序列S=[s1,s2,⋅⋅⋅sn]，假定每个数字互不相同，如果其子序列[s(i1),s(i2),⋅⋅⋅,s(ik)]满足1≤i1<i2<⋅⋅⋅<ik≤n，s(i1)<s(i2)<⋅⋅⋅<s(ik)，则称为上升子序列。
"""


def run(nums):
    lenn = len(nums)
    dp = [1] * lenn
    for i in range(lenn):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    print(dp)
    return max(dp)


inp = [1, 3, 4, 2, 7, 9, 6, 8]
res = run(inp)
print(res)

"""
面试题 11：旋转数组的最小数字
题目：把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如数组
{3, 4, 5, 1, 2} 为 {1, 2, 3, 4, 5} 的一个旋转，该数组的最小值为 1。

"""

def find_min(lst: list) -> int:
    if not lst:
        return None
    beg, end = 0, len(lst) - 1
    # 若干个为 0，即依然是原数组
    if lst[end] > lst[beg]:
        res = lst[beg]
    elif lst[end] == lst[beg]:
        res = min_in_order(lst)
    else:
        while lst[end] < lst[beg]:
            if end - beg == 1:
                res = lst[end]
                break
            mid = (end + beg) // 2
            if lst[mid] > lst[beg]:
                beg = mid
            else:
                end = mid
    return res

def min_in_order(lst: list) -> int:
    res = lst[0]
    for i in lst:
        if i < res:
            res = i
    return res

def findMin(nums: list) -> int:
    if not nums:
        return None
    if len(nums) == 1:
        return nums[0]
    lt, rt = 0, len(nums) - 1
    while lt <= rt:
        mid = (lt + rt) // 2
        if nums[mid] > nums[mid+1]:
            return nums[mid+1]
        else:
            if nums[mid] > nums[-1]:
                lt = mid + 1
            else:
                rt = mid - 1
    return nums[0]


if __name__ == '__main__':
    lst = [ 3, 4, 5, 1, 1, 2 ]
    print(find_min(lst))
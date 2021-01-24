"""
面试题 53（四）：数组中数值只出现一次的数
题目：假设一个单调递增的数组里的除一个元素只出现一次外，其他每个元素都出现了两次。
例如，在数组 {1, 1, 2, 3, 3} 中，数字 2 只出现了一次。
假设数组至少有两个元素。

"""

def find(lst):
    if len(lst) == 2 and lst[0] == lst[1]:
        return -1
    if lst[0] != lst[1]:
        return lst[0]
    if lst[-1] != lst[-2]:
        return lst[-1]
    start, end = 0, len(lst) - 1
    while start <= end:
        mid = (start + end) // 2
        if lst[mid] == lst[mid-1]:
            if mid % 2 == 0:
                end = mid - 1
            else:
                start = mid + 1
        elif lst[mid] == lst[mid+1]:
            if mid % 2 == 0:
                start = mid + 1
            else:
                end = mid - 1
        else:
            return lst[mid]


if __name__ == '__main__':
    lst = [1,1,2,2,3,4,4,5,5,6,6]
    res = find(lst)
    print(res)
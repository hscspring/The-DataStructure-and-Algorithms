"""
面试题 66：构建乘积数组
题目：给定一个数组 A [0, 1, …, n-1]，请构建一个数组 B [0, 1, …, n-1]，其
中 B 中的元素 B [i] =A [0]×A [1]×… ×A [i-1]×A [i+1]×…×A [n-1]。不能使用除法。
"""

def build_production_array(arr: list) -> list:
    """
    
    Parameters
    -----------

    Returns
    ---------


    Notes
    ------

    """
    if not arr:
        return arr

    lenth = len(arr)
    out = [1] * lenth
    for i in range(1, lenth):
        out[i] = out[i-1] * arr[i-1]
    tmp = 1
    for i in range(lenth-2, -1, -1):
        tmp *= arr[i+1]
        out[i] *= tmp
    return out


def product_array(lst: list) -> list:
    length = len(lst)
    arr1 = [1] * length
    # 下三角 [1, 2, 6]
    for i in range(1, length):
        arr1[i] =  lst[i-1] * arr1[i-1]
    arr2 = [1] * length
    for i in range(length-2, -1, -1):
        arr2[i] = lst[i+1] * arr2[i+1]
    
    for i in range(length):
        arr1[i] = arr1[i] * arr2[i]
    return arr1


if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5]
    res = build_production_array(lst)
    print(res)








    
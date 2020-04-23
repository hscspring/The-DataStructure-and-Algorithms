"""
面试题 61：扑克牌的顺子
题目：从扑克牌中随机抽 5 张牌，判断是不是一个顺子，即这 5 张牌是不是连续的。
2～10 为数字本身，A 为 1，J 为 11，Q 为 12，K 为 13，而大、小王可以看成任意数字。

"""

def dct_sort(ls: list, dct: dict) -> list:
    for i in lst:
        dct[i] += 1
    res = []
    for i,v in dct.items():
        if v > 0:
            res.extend([i]*v)
    return res

def is_continous(lst: list) -> bool:
    """
    

    Parameters
    -----------
    lst: the given five cards

    Returns
    ---------
    out: whether the given cards is continous


    Notes
    ------

    """
    if len(lst) < 5:
        return False
    
    start, end = 0, 13
    dct = dict(zip(range(start, end+1), [0]*(end+1-start)))

    for i in lst:
        dct[i] += 1
    zero_num = dct[0]
    
    nonzero = []
    for i,v in dct.items():
        if i == 0:
            continue
        
        if v > 1:
            return False
        elif v == 1:
            nonzero.append(i)
    
    if nonzero:
        miss_num = (nonzero[-1]+1 - nonzero[0]) - len(nonzero)
    else:
        miss_num = 0
    
    return zero_num >= miss_num



def dct_sort(lst: list):
    res = []
    dct = dict(zip(range(14), [0]*14))
    for i in lst:
        dct[i] += 1
    for k,v in dct.items():
        res.extend([k] * v)
    return res

def is_continous2(lst: list):
    if len(lst) < 5:
        return False
    sorted_lst = dct_sort(lst)
    num_zero = 0
    num_gap = 0
    length = len(sorted_lst)
    for i in range(length-1):
        if sorted_lst[i] == 0:
            num_zero += 1
        else:
            if sorted_lst[i] == sorted_lst[i+1]:
                return False
            else:
                num_gap += sorted_lst[i+1] - sorted_lst[i] - 1
    return num_zero >= num_gap




if __name__ == '__main__':
    lst = [1, 0, 0, 7, 0]
    res = is_continous(lst)
    print(res)







    
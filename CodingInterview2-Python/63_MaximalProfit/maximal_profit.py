"""
面试题 63：股票的最大利润
题目：假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖交易该股
票可能获得的利润是多少？例如一只股票在某些时间节点的价格为 {9, 11, 8, 5,
7, 12, 16, 14}。如果我们能在价格为 5 的时候买入并在价格为 16 时卖出，则能
收获最大的利润 11。
"""

def get_max_diff(lst: list) -> int:
    """
    

    Parameters
    -----------
    lst: price list.

    Returns
    ---------
    out: the max diff


    Notes
    ------

    """
    if len(lst) < 2:
        return 0
    minv = lst[0]
    diff = lst[1] - minv
    for i in range(2, len(lst)):
        if lst[i-1] < minv:
            minv = lst[i-1]
        curr_diff = lst[i] - minv
        if curr_diff > diff:
            diff = curr_diff
    return diff





if __name__ == '__main__':
    lst = [16, 11, 7, 4, 2, 1]
    
    res = get_max_diff(lst)
    print(res)








    
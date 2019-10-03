"""
面试题 56（二）：数组中唯一只出现一次的数字
题目：在一个数组中除了一个数字只出现一次之外，其他数字都出现了三次。请
找出那个吃出现一次的数字。

"""



def find_num_appear_once(lst: list) -> int:
    """
    
    
    Parameters
    -----------
    lst: the given list, with one num appear once, the others appear thrice.

    Returns
    ---------
    out: the num only appear once.


    Notes
    ------
    二进制的每一位加起来，分别 % 3 就是出现 1 次的那个数的二进制
    use dict is easy, but cost O(n) space.
    """
    if not lst:
        return None

    prev = '0'
    minus_count = 0
    zero_count = 0
    for v in lst:
        if v < 0:
            minus_count += 1
        if v == 0:
            zero_count += 1


        curr = get_binary(v)
        lencr, lenpe, = len(curr), len(prev)
        max_len = max(lencr, lenpe)
        if lencr > lenpe:
            prev = prev.zfill(max_len)
        else:
            curr = curr.zfill(max_len)
        
        tmp = []
        for i in range(max_len):
            tmp.append(int(prev[i]) + int(curr[i]))

        prev = "".join(map(str, tmp))
    
    tmp = []
    for v in prev:
        tmp.append(int(v)%3)
    res = int("".join(map(str, tmp)), 2)

    if res == 0 and zero_count == 0:
        return None

    if minus_count % 3 == 1:
        return -res

    return res


    
def get_binary(num: int) -> str:
    if num > 0:
        return bin(num)[2:]
    else:
        return bin(num)[3:]



if __name__ == '__main__':
    data = [ -10, 214, 214, 214 ]
    res = find_num_appear_once(data)
    print(res)













    
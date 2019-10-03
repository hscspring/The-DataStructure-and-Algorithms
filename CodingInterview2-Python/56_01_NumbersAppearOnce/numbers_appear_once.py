"""
面试题 56（一）：数组中只出现一次的两个数字
题目：一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序
找出这两个只出现一次的数字。要求时间复杂度是 O (n)，空间复杂度是 O (1)。

"""



def find_num_appear_once(lst: list) -> list:
    """
    
    
    Parameters
    -----------
    lst: the given list, with two nums appear once, the others appear twice.

    Returns
    ---------
    out: nums only appear once.


    Notes
    ------
    任何一个数字异或自己都等于0
    num ^ num == 0
    """
    if not lst:
        return []
    
    xor = 0
    for v in lst:
        xor = xor ^ v

    firt_one_index = last_bit_one_index(xor)
    
    if not firt_one_index:
        return []

    xor1, xor2 = 0, 0
    for v in lst:
        if is_bit_one(v, firt_one_index):
            xor1 = xor1 ^ v
        else:
            xor2 = xor2 ^ v

    return [xor2, xor1]


def last_bit_one_index(num: int) -> int:
    res = 0
    while num & 1 == 0 and res < 32:
        num = num >> 1
        res += 1
    if res == 0 or res >= 32:
        return None
    return res

def is_bit_one(num: int, index: int) -> bool:
    num = num >> index
    return num & 0x01

def last_bit_one_index2(num: int) -> int:
    binary = bin(num)
    for i in range(1, len(binary)+1):
        if binary[-i] == '1':
            return -i
    return None

def is_bit_one2(num: int, index: int) -> bool:
    binary = bin(num)
    if index >= len(binary):
        return False
    else:
        return binary[index] == '1'


if __name__ == '__main__':
    data = [ 1,1,2,2 ]
    res = find_num_appear_once(data)
    print(res)

    print(first_bit_one_index(0))
    print(is_bit_one(0, 8))














    
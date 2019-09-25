"""
面试题 44：数字序列中某一位的数字
题目：数字以 0123456789101112131415… 的格式序列化到一个字符序列中。在这
个序列中，第 5 位（从 0 开始计数）是 5，第 13 位是 1，第 19 位是 4，等等。请写一
个函数求任意位对应的数字。

"""



def digit_at_index(index: str) -> str:
    """
    

    Parameters
    -----------

    Returns
    ---------


    Notes
    ------
    The given digits are a series of 0..n

    """
    if index < 0:
        return -1

    digits, num_digits = 1, 10 
    while index >= num_digits: 
        index -= num_digits
        digits += 1
        nums = 9 * 10 ** (digits - 1)
        num_digits = digits * nums

    num = 10 ** (digits-1) + index // digits
    index_from_right = digits - index % digits

    for i in range(1, index_from_right):
        num //= 10

    return num % 10


if __name__ == '__main__':
    res = digit_at_index(13)
    res = digit_at_index(19)
    res = digit_at_index(10)
    res = digit_at_index(189)
    res = digit_at_index(190)
    res = digit_at_index(12)
    print(res)













    
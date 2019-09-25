"""
面试题 45：把数组排成最小的数
题目：输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼
接出的所有数字中最小的一个。例如输入数组 {3, 32, 321}，则打印出这 3 个数
字能排成的最小数字 321323。

"""

from functools import cmp_to_key


def combine_to_min_num(lst: list) -> str:
    """


    Parameters
    -----------

    Returns
    ---------


    Notes
    ------

    """
    res = "".join(sorted(map(str, lst),
                         key=cmp_to_key(lambda m, n: int(m+n)-int(n+m))))
    while res and res[0] == "0":
        res = res[1:]
    return res


# def compare(m: str, n: str) -> int:
#     return int(m+n) - int(n+m)


if __name__ == '__main__':
    lst = [3, 32, 321]
    # lst = [9, 18, 0, 0]
    res = combine_to_min_num(lst)
    print(res)

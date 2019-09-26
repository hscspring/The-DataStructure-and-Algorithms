"""

面试题49：丑数
题目：我们把只包含因子2、3和5的数称作丑数（Ugly Number）。求按从小到
大的顺序的第1500个丑数。例如6、8都是丑数，但14不是，因为它包含因子7。
习惯上我们把1当做第一个丑数。
"""




def get_ugly(n: int) -> int:
    """
    Get nth ugly number.

    Parameters
    -----------

    Returns
    ---------
    

    Notes
    ------

    """
    if n <= 0:
        return 0
    uglies = [1]  + [0] * (n-1)
    nxt, u2, u3, u5 = 1, 0, 0, 0
    while nxt < n:
        minn = min(uglies[u2]*2, uglies[u3]*3, uglies[u5]*5)
        uglies[nxt] = minn
        
        while uglies[u2]*2 <= uglies[nxt]:
            u2 += 1
        while uglies[u3]*3 <= uglies[nxt]:
            u3 += 1
        while uglies[u5]*5 <= uglies[nxt]:
            u5 += 1

        nxt += 1
    return uglies[-1]



def get_ugly_naive(n: int) -> int:
    if n <= 0:
        return 0
    index, num = 0, 0
    while index < n:
        num += 1
        if is_ugly(num):
            index += 1
    return num

def is_ugly(num: int) -> bool:
    while num % 2 == 0:
        num /= 2
    while num % 3 == 0:
        num /= 3
    while num % 5 == 0:
        num /= 5
    return num == 1


if __name__ == '__main__':
    num = 859963392
    res = is_ugly(num)
    res = get_ugly(1500)
    print(res)













    
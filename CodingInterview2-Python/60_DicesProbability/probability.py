"""
面试题 60：n 个骰子的点数
题目：把 n 个骰子扔在地上，所有骰子朝上一面的点数之和为 s。输入 n，打印出 s
的所有可能的值出现的概率。

"""

max_val = 6

def get_probability_recursion(n: int) -> int:
    """
    

    Parameters
    -----------
    n: the num of dices.

    Returns
    ---------


    Notes
    ------

    """
    if n <= 0:
        return 0
    total = max_val ** n
    # 6 ~ 6n
    freq = [0] * (max_val * n - n + 1)
    for i in range(1, max_val+1):
        freq = probability(n, n, i, freq)
    # res = {}
    # for i in range(n, 6*n+1):
    #     res[i] = freq[i-n]/total
    print(freq)
    return sum(freq) - total

def probability(n: int, curr: int, sums: int, freq: list):
    if curr == 1:
        freq[sums-n] += 1
    else:
        for i in range(1, max_val+1):
            probability(n, curr-1, i+sums, freq)
    return freq



def get_probability_recursion2(n: int) -> int:
    if n <= 0:
        return 0
    total = max_val ** n
    freq = get_freq(n, n, 1, [0] * (max_val * n - n + 1))
    return total - sum(freq)


def get_freq(n: int, curr: int, sums: int, freq: list):
    """This solution is easier to understand"""
    for i in range(1, max_val+1):
        if curr == 1:
            freq[i-n] += 1
        else:
            for j in range(1, max_val+1):
                probability(n, curr-1, i+j, freq)
    return freq


def get_probability(n: int) -> int:
    if n <= 0:
        return 0
    # the nth num is the freq of sum n
    # 加一个新骰子后，一个数组的第 n 项（和为 n 的次数）等于另一个数组的 n-1 ~ n-6 项之和
    freq1 = [0] + [1] * max_val + [0] * (max_val*(n-1))
    freq2 = [0] + [0] * (max_val*n)
    total = max_val ** n
    flag = 0
    for k in range(2, n+1):
        if not flag:
            for i in range(k):
                freq2[i] = 0
            for i in range(k, max_val*k+1):
                freq2[i] = 0
                for j in range(1, max_val+1):
                    if j <= i:
                        freq2[i] += freq1[i-j]
            flag = 1
        else:
            for i in range(k):
                freq1[i] = 0
            for i in range(k, max_val*k+1):
                freq1[i] = 0
                for j in range(1, max_val+1):
                    if j <= i:
                        freq1[i] += freq2[i-j]
            flag = 0
    freq = freq2[n:] if flag else freq1[n:]
    return sum(freq) - total


if __name__ == '__main__':
    n = 2
    res = get_probability_recursion(n)
    print(res)

    # n = 3
    # freq = [0] * (6 * n - n + 1)
    # print(probability(n, n, 1, freq))


    # print(prob(n, n, 1, freq))

    res = get_probability_recursion2(n)
    print(res)


    res = get_probability(n)
    print(res)










    
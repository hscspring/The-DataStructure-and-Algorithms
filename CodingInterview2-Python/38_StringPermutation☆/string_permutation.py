"""
面试题 38：字符串的排列
题目：输入一个字符串，打印出该字符串中字符的所有排列。例如输入字符串 abc，
则打印出由字符 a、b、c 所能排列出来的所有字符串 abc、acb、bac、bca、cab 和 cba。

"""



def permutate1(s: str) -> list:
    """
    Permutate a given string.

    Parameters
    -----------
    s: the given string

    Returns
    ---------
    out: all the permutation of the given string

    Notes
    ------

    """
    if not s:
        return []
    return permutate_core1(list(s), 0, len(s), [])


def permutate_core1(lst: list, l: int, r: int, res: list) -> list:
    # https://www.youtube.com/watch?v=AfxHGNRtFac
    if l == r - 1:
        item = "".join(lst)
        if item not in res:
            res.append(item)
    else:
        for i in range(l, r):
            lst[l], lst[i] = lst[i], lst[l]
            permutate_core1(lst, l+1, r, res)
            lst[i], lst[l] = lst[l], lst[i]
    return res


def permutate3(s: str) -> list:
    if not s:
        return []
    return permutate_core3(s, 0, len(s), [])

def permutate_core3(s, l, r, res) -> list:
    # https://www.youtube.com/watch?v=KBHFyg2AcZ4
    if l == r - 1:
        if s not in res:
            res.append(s)
    else:
        for i in range(l, r):
            lst = list(s)
            lst[i], lst[l] = lst[l], lst[i]
            permutate_core3("".join(lst), l+1, r, res)
            lst[l], lst[i] = lst[i], lst[l]
    return res



def permutate2(s: str) -> list:
    if not s:
        return []
    return permutate_core2(s, [], [])

def permutate_core2(s: str, moves: list, res: list) -> list:
    for i in range(len(s)):
        remain = s[0:i] + s[i+1:]
        moves.append(s[i])
        if remain:
            permutate_core2(remain, moves, res)
        else:
            res.append("".join(moves))
        moves.pop()
    return res


def help_func(s):
    # for the eight queens puzzle
    n = len(s)
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if i - j == int(s[i]) - int(s[j]) or j - i == int(s[i]) - int(s[j]):
                return False
    return True



def permutate4(iterable, r=None):
    # from https://docs.python.org/3.7/library/itertools.html
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = list(range(n))
    cycles = list(range(n, n-r, -1))
    yield "".join(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield "".join(pool[i] for i in indices[:r])
                break
        else:
            return

def product(*args, repeat=1):
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
    pools = [tuple(pool) for pool in args] * repeat
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)

def permutate5(iterable, r=None):
    # from https://docs.python.org/3.7/library/itertools.html
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    for indices in product(range(n), repeat=r):
        if len(set(indices)) == r:
            yield "".join(pool[i] for i in indices)


def permutate6(s: str) -> list:
    # https://www.youtube.com/watch?v=hqijNdQTBH8
    lst = list(s)
    if not lst:
        # return []
        yield []
    elif len(lst) == 1:
        # return [lst]
        yield lst
    else:
        res = []
        for i in range(len(lst)):
            head = lst[i]
            remain = lst[:i] + lst[i+1:]
            for p in permutate5(remain):
                # res.append([head] + p)
                yield [head] + p
        # return res


def permutate7(s: str) -> list:
    if not s:
        return []
    return permutate_core7("", s, [])

def permutate_core7(prefix, suffix, res) -> list:
    # https://www.youtube.com/watch?v=IPWmrjE1_MU
    if not suffix:
        res.append(prefix)
    else:
        for i in range(len(suffix)):
            # print(prefix, suffix, i,prefix+suffix[i], suffix[:i]+suffix[i+1:], res)
            permutate_core7(prefix+suffix[i], suffix[:i]+suffix[i+1:], res)
    return res


if __name__ == '__main__':
    s = [str(i) for i in range(3)]
    s = "abc"
    # res = permutate_core(s, [], [])
    # print(res)

    res = permutate7(s)
    print((list(res)))

    # res = permutations1(s)
    # print(len(list(res)))













    
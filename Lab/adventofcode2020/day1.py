import pnlp


file = "day1.txt"

nums = list(map(int, pnlp.read_lines(file)))
year = 2020

def add_two_is(year: int, nums: list) -> int:
    lst = []

    for i in nums:
        if year - i in nums:
            lst.append((i, year-i))

    res = []
    for pair in lst:
        res.append(pair[0] * pair[1])

    return (max(res))


def add_three_is(year: int, nums: list) -> int:

    lst = set()
    for i in nums:
        need = year - i
        for j in nums:
            if need - j in nums:
                pair = sorted((i, j, need-j))
                lst.add(tuple(pair))
    res = []
    for pair in lst:
        res.append(pair[0] * pair[1] * pair[2])
    return max(res)

res = add_three_is(year, nums)

print(res)



import pnlp


file = "data/day18.txt"


def is_op(x):
    return x in ["+", "*", "(", ")"]


def get_curr(x):
    if is_op(x):
        return x
    return int(x)


def calc(ops, nums, reverse=False):
    if reverse:
        ops = list(reversed(ops))
        nums = list(reversed(nums))
    res = nums.pop()
    while nums and ops:
        op = ops.pop()
        num = nums.pop()
        if op == "*":
            res *= num
        elif op == "+":
            res += num
    return res


def calc2(ops, nums, reverse=False):
    if reverse:
        ops = list(reversed(ops))
        nums = list(reversed(nums))
    new_nums, new_ops = [], []
    last = nums.pop()
    while nums and ops:
        op = ops.pop()
        num = nums.pop()
        if op == "*":
            new_nums.append(last)
            last = num
        elif op == "+":
            last += num
    new_nums.append(last)
    res = 1
    for i in new_nums:
        res *= i
    return res

def calc_line(line, calc=calc):
    line = line.replace(" ", "")
    nums = []
    ops = []
    length = len(line)
    i = 0
    while i < length:
        v = line[i]
        i += 1
        curr = get_curr(v)
        if is_op(v):
            if curr != ")":
                ops.append(curr)
            else:
                k = 0
                new_ops = []
                new_nums = []
                x = ops.pop()
                while x != "(":
                    k += 1
                    new_ops.append(x)
                    x = ops.pop()
                for _ in range(k+1):
                    x = nums.pop()
                    new_nums.append(x)
                tmp = calc(new_ops, new_nums)
                nums.append(tmp)
        else:
            nums.append(curr)
    return calc(ops, nums, reverse=True)


line = "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"
assert calc_line(line) == 13632
assert calc_line(line, calc2) == 23340

line = "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"
assert calc_line(line) == 12240
assert calc_line(line, calc2) == 669060

line = "5 + (8 * 3 + 9 + 3 * 4 * 3)"
assert calc_line(line) == 437
assert calc_line(line, calc2) == 1445

line = "2 * 3 + (4 * 5)"
assert calc_line(line) == 26
assert calc_line(line, calc2) == 46

line = "1 + (2 * 3) + (4 * (5 + 6))"
assert calc_line(line) == 51
assert calc_line(line, calc2) == 51

line = "1 + 2 * 3 + 4 * 5 + 6"
assert calc_line(line) == 71
assert calc_line(line, calc2) == 231

lines = pnlp.read_lines(file)
res = 0
for line in lines:
    res += calc_line(line, calc2)
print(res)

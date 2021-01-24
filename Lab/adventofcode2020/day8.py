import pnlp
import copy

file = "day8Test.txt"
file = "day8.txt"

lines = pnlp.read_lines(file)

lst = [1, 2, 3, 4, 5]


def inf_loop(lst: list, start: int, n: int):
    length = len(lst)
    assert start < length
    if n < 0:
        length - n % length
    reminder = n % length
    idx = (start + reminder) % length
    return idx


assert inf_loop(list(range(8)), 2, 4) == 6
assert inf_loop(lst, 0, 10) == 0
assert inf_loop(lst, 1, 10) == 1
assert inf_loop(lst, 1, 11) == 2
assert inf_loop(lst, 4, 11) == 0
assert inf_loop(lst, 4, -3) == 1
assert inf_loop(lst, 3, -13) == 0


def read_line(line):
    op, num = line.split()
    sign = num[0]
    val = int(num[1:])
    if sign == "-":
        val = -val
    return op, val


def repeat_loop_acc(lines):
    dct = dict(zip(range(len(lines)), [0]*len(lines)))
    length = len(lines)
    repeat = False
    acc = 0
    i = 0
    time = dct.get(i)
    while i < length and time == 0:
        sign, val = read_line(lines[i])
        dct[i] += 1
        if sign == "acc":
            acc += val
            i += 1
        elif sign == "jmp":
            # i = inf_loop(lines, i, val)
            i += val
        else:
            i += 1
        time = dct.get(i)
        if time and time > 0:
            repeat = True
            break
    return acc, repeat


res = repeat_loop_acc(lines)
print(res)


for i,line in enumerate(lines):
    tmp = line.split()
    if tmp[0] == "nop":
        new = "jmp" + " " + tmp[1]
    elif tmp[0] == "jmp":
        new = "nop" + " " + tmp[1]
    else:
        continue
    new_lines = lines[:i] + [new] + lines[i+1:]
    acc, repeat = repeat_loop_acc(new_lines)
    if repeat == False:
        print(acc, repeat)







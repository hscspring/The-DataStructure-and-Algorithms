import pnlp
from pprint import pprint


def occ_around_num1(
        lines: list, row: int, col: int, rows: int, cols: int) -> int:
    up = row - 1, col
    down = row + 1, col
    left = row, col - 1
    right = row, col + 1
    leftup = row - 1, col - 1
    rightup = row - 1, col + 1
    leftdown = row + 1, col - 1
    rightdown = row + 1, col + 1
    num = 0
    for x, y in [up, down, left, right, leftup, rightup, leftdown, rightdown]:
        if x < 0 or x >= rows or y < 0 or y >= cols:
            continue
        if lines[x][y] == "#":
            num += 1
    return num


def get_up(row: int, col: int, bound: int) -> tuple:
    while row > bound and lines[row][col] == ".":
        row -= 1
    return row, col

def get_down(row: int, col: int, bound: int) -> tuple:
    while row < bound - 1 and lines[row][col] == ".":
        row += 1
    return row, col

def get_left(row: int, col: int, bound: int) -> tuple:
    while col > bound and lines[row][col] == ".":
        col -= 1
    return row, col

def get_right(row: int, col: int, bound: int) -> tuple:
    while col < bound - 1 and lines[row][col] == ".":
        col += 1
    return row, col


def get_leftup(row: int, col: int, rb: int, cb: int) -> tuple:
    while row > rb and col > cb and lines[row][col] == ".":
        row -= 1
        col -= 1
    return row, col


def get_rightup(row: int, col: int, rb: int, cb: int) -> tuple:
    while row > rb and col < cb - 1 and lines[row][col] == ".":
        row -= 1
        col += 1
    return row, col


def get_leftdown(row: int, col: int, rb: int, cb: int) -> tuple:
    while row < rb - 1 and col > cb and lines[row][col] == ".":
        row += 1
        col -= 1
    return row, col


def get_rightdown(row: int, col: int, rb: int, cb: int) -> tuple:
    while row < rb - 1 and col < cb - 1 and lines[row][col] == ".":
        row += 1
        col += 1
    return row, col


def occ_around_num2(
    lines: list, row: int, col: int, rows: int, cols: int) -> int:
    up = get_up(row - 1, col, 0)
    down = get_down(row + 1, col, rows)
    left = get_left(row, col - 1, 0)
    right = get_right(row, col + 1, cols)

    leftup = get_leftup(row - 1, col - 1, 0, 0)
    rightup = get_rightup(row - 1, col + 1, 0, cols)
    leftdown = get_leftdown(row + 1, col - 1, rows, 0)
    rightdown = get_rightdown(row + 1, col + 1, rows, cols)

    num = 0
    for x, y in [up, down, left, right, leftup, rightup, leftdown, rightdown]:
        if x < 0 or x >= rows or y < 0 or y >= cols:
            continue
        if lines[x][y] == "#":
            num += 1
    return num


def init(rows: int, cols: int):
    res = []
    for i in range(rows):
        tmp = []
        for j in range(cols):
            tmp.append("")
        res.append(tmp)
    return res


def one_round(lines: list, rows: int, cols: int, tolerant: int, occ_round):
    initial = init(rows, cols)
    for row, line in enumerate(lines):
        for col, v in enumerate(line):
            if v == "L" and occ_round(lines, row, col, rows, cols) == 0:
                initial[row][col] = "#"
            elif v == "#" and occ_round(lines, row, col, rows, cols) >= tolerant:
                initial[row][col] = "L"
            else:
                initial[row][col] = v
    return initial


def to_string(lst: list):
    res = []
    for row in lst:
        tmp = "".join(row)
        res.append(tmp)
    return "".join(res)


def equal(first: list, second: list):
    s1 = to_string(first)
    s2 = to_string(second)
    return s1 == s2



file = "data/day11Test.txt"
file = "data/day11.txt"

lines = pnlp.read_lines(file)
rows = len(lines)
cols = len(lines[0])


round_res = lines
last = init(rows, cols)
while not equal(last, round_res):
    last = round_res
    # round_res = one_round(round_res, rows, cols, 4, occ_around_num1)
    round_res = one_round(round_res, rows, cols, 5, occ_around_num2)


res = to_string(round_res)
print(res.count("#"))









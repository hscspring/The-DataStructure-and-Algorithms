import pnlp

DIRECTS = ["E", "S", "W", "N"]
SIGNS = ["++", "+-", "--", "-+"]


def get_direct(directs: list, direct: str, num: int, rotate: str):
    count = num // 90
    idx = directs.index(direct)
    if rotate == "R":
        new_idx = idx + count
        return directs[new_idx % 4]
    else:
        new_idx = idx - count
        return directs[new_idx]


assert get_direct(DIRECTS, "E", 90, "R") == "S"
assert get_direct(DIRECTS, "E", 90, "L") == "N"
assert get_direct(DIRECTS, "S", 270, "R") == "E"
assert get_direct(DIRECTS, "S", 270, "L") == "W"


file = "data/day12Test.txt"
# file = "data/day12.txt"


def get_dist(file):
    lines = pnlp.read_lines(file)
    x, y = 0, 0
    direct = "E"
    for line in lines:
        nvi = line[0]
        num = int(line[1:])
        if nvi == "R":
            direct = get_direct(DIRECTS, direct, num, "R")
        elif nvi == "L":
            direct = get_direct(DIRECTS, direct, num, "L")
        else:
            if nvi == "F":
                tmp = direct
            else:
                tmp = nvi

            if tmp == "N":
                y += num
            elif tmp == "S":
                y -= num
            elif tmp == "W":
                x -= num
            elif tmp == "E":
                x += num
    return abs(x) + abs(y)


def get_sign(dx, dy):
    if dx >= 0 and dy >= 0:
        return "++"
    elif dx >= 0 and dy <= 0:
        return "+-"
    elif dx <= 0 and dy >= 0:
        return "-+"
    elif dx <= 0 and dy <= 0:
        return "--"


def get_waypoint(dx, dy, num, rotate):
    sign = get_sign(dx, dy)
    # 判断第几象限，x 和 y 的符号
    new_sign = get_direct(SIGNS, sign, num, rotate)
    sg1 = new_sign[0]
    sg2 = new_sign[1]
    # 判断是否需要交换 x 和 y
    if num == 90 or num == 270:
        dx, dy = abs(dy), abs(dx)
    else:
        dx, dy = abs(dx), abs(dy)
    return int(sg1 + str(dx)), int(sg2 + str(dy))


assert get_waypoint(1, 5, 0, "R") == (1, 5)
assert get_waypoint(1, 5, 360, "L") == (1, 5)
assert get_waypoint(1, 5, 90, "R") == (5, -1)
assert get_waypoint(1, 5, 270, "L") == (5, -1)
assert get_waypoint(1, 5, 180, "R") == (-1, -5)
assert get_waypoint(1, 5, 180, "L") == (-1, -5)


assert get_waypoint(1, 0, 0, "R") == (1, 0)
assert get_waypoint(1, 0, 360, "L") == (1, 0)
assert get_waypoint(1, 0, 90, "R") == (0, -1)
assert get_waypoint(1, 0, 270, "L") == (0, -1)
assert get_waypoint(1, 0, 180, "R") == (-1, 0)
assert get_waypoint(1, 0, 180, "L") == (-1, 0)


assert get_waypoint(2, -15, 180, "R") == (-2, 15)
assert get_waypoint(-2, 15, 90, "L") == (-15, -2)
assert get_waypoint(2, -15, 270, "R") == (15, 2)


lines = pnlp.read_lines(file)
x, y = 0, 0
dx, dy = 10, 1
for line in lines:
    nvi = line[0]
    num = int(line[1:])
    if nvi == "R":
        dx, dy = get_waypoint(dx, dy, num, "R")
    elif nvi == "L":
        dx, dy = get_waypoint(dx, dy, num, "L")
    elif nvi in DIRECTS:
        if nvi == "N":
            dy += num
        elif nvi == "S":
            dy -= num
        elif nvi == "W":
            dx -= num
        elif nvi == "E":
            dx += num
    elif nvi == "F":
        x += num * dx
        y += num * dy
    # print(line, dx, dy, x, y)
print(abs(x) + abs(y))

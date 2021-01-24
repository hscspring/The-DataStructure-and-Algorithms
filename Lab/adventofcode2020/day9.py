import pnlp


def get_target(win: int, lines: list):
    for i in range(win, len(lines)):
        target = lines[i]
        pool = lines[i-win: i]
        can = False
        for j in pool:
            if target - j in pool:
                can = True
                break
        if can == False:
            return target
    return None

file = "day9.txt"
win = 25

file = "day9Test.txt"
win = 5

lines = pnlp.read_lines(file)
lines = list(map(int, lines))

target = get_target(win, lines)
print(target)

def get_min_max_sum(target: int, lines: list):
    slide = []
    for i in lines:
        slide.append(i)
        while sum(slide) > target:
            slide.pop(0)
        if sum(slide) == target and len(slide) > 1:
            return min(slide) + max(slide)

res = get_min_max_sum(target, lines)
print(res)
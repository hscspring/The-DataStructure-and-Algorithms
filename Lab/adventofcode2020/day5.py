
import pnlp
import math


def bs(s: int, e: int, typ: str):
    mid = (s + e) // 2

    if typ in ["F", "L"]:
        e = mid
    else:
        s = mid
    if s % 2 == 1:
        s += 1
    return (s, e)


def get_seatid(string: str) -> int:
    s, e = 0, 127
    for t in string[:-3]:
        s, e = bs(s, e, t)
    row = e

    s, e = 0, 7
    for t in string[-3:]:
        s, e = bs(s, e, t)
    col = e

    return row * 8 + col


for s in ["FBFBBFFRLR", "BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]:
    res = get_seatid(s)
    print(res)


lines = pnlp.read_lines("day5.txt")
ids = set()
for line in lines:
    id = get_seatid(line)
    ids.add(id)

print()
print(max(ids))
mx = max(ids)
mn = min(ids)


for i in range(mn+1, mx):
    if i not in ids:
        print(i)
        break

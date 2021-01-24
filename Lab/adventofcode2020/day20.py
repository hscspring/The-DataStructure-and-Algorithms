import pnlp
from collections import Counter
from itertools import chain

LOCS = ["up", "down", "left", "right"]

file = "data/day20.txt"
# file = "data/day20Test.txt"


def get_dct(file):
    txt = pnlp.read_file(file)
    dct = {}
    for part in txt.split("\n\n"):
        part = part.strip()
        lst = part.split("\n")
        key = lst[0].replace(":", "").split()[1]
        key = int(key)
        dct[key] = lst[1:]
    return dct


def get_count(dct):
    lst = []
    for key in dct:
        val = dct[key]
        up = val[0]
        down = val[-1]
        left = "".join([i[0] for i in val])
        right = "".join([i[-1] for i in val])
        rev_up = "".join(reversed(up))
        rev_down = "".join(reversed(down))
        rev_left = "".join(reversed(left))
        rev_right = "".join(reversed(right))
        lst.append(up)
        lst.append(down)
        lst.append(left)
        lst.append(right)
        lst.append(rev_up)
        lst.append(rev_down)
        lst.append(rev_left)
        lst.append(rev_right)
    count = Counter(lst)
    return count


def satisfied_edges(count, locs):
    res = []
    for i, v in enumerate(locs):
        cou = count.get(v, 0)
        if cou >= 2:
            loc = LOCS[i]
            res.append(loc)
    return res


def get_edges(sq: list):
    up = sq[0]
    down = sq[-1]
    left = "".join([i[0] for i in sq])
    right = "".join([i[-1] for i in sq])
    return (up, down, left, right)


def get_kinds_edges(dct, count):
    corners = []
    borders = []
    inners = []
    for key in dct:
        val = dct[key]
        edges = get_edges(val)
        sati_edges = satisfied_edges(count, edges)
        if len(sati_edges) == 2:
            corners.append(key)
        elif len(sati_edges) == 3:
            borders.append(key)
        else:
            inners.append(key)
    return corners, borders, inners


def get_prod(corners):
    x = 1
    for key in corners:
        x *= key
    return x


dct = get_dct(file)
count = get_count(dct)
corners, borders, inners = get_kinds_edges(dct, count)
res = get_prod(corners)
print("part1 result: ", res)
print("corners: ", corners)
print("length borders, inners: ", len(borders), len(inners))
print("++"*20)


def flip_ud(sq: list):
    up = sq[-1]
    down = sq[0]
    left = "".join(reversed([i[0] for i in sq]))
    right = "".join(reversed([i[-1] for i in sq]))
    return (up, down, left, right)


def flip_lr(sq: list):
    up = "".join(reversed(sq[0]))
    down = "".join(reversed(sq[-1]))
    left = "".join(reversed([i[-1] for i in sq]))
    right = "".join(reversed([i[0] for i in sq]))
    return (up, down, left, right)


def rotate_90(sq: list):
    up = "".join(reversed([i[0] for i in sq]))
    down = "".join(reversed([i[-1] for i in sq]))
    left = "".join(sq[-1])
    right = "".join(sq[0])
    return (up, down, left, right)

def rotate_180(sq: list):
    up = "".join(reversed(sq[-1]))
    down = "".join(reversed(sq[0]))
    left = "".join(reversed([i[-1] for i in sq]))
    right = "".join(reversed([i[0] for i in sq]))
    return (up, down, left, right)

def rotate_270(sq: list):
    up = "".join([i[-1] for i in sq])
    down = "".join([i[0] for i in sq])
    left = "".join(reversed(sq[0]))
    right = "".join(reversed(sq[-1]))
    return (up, down, left, right)

def flip_ud_rotate_90(sq):
    up, down, left, right = flip_ud(sq)
    return rotate_90([up, down])

def filp_ud_rotate_180(sq):
    up, down, left, right = flip_ud(sq)
    return rotate_180([up, down])

def flip_ud_rotate_270(sq):
    up, down, left, right = flip_ud(sq)
    return rotate_270([up, down])

def flip_lr_rotate_90(sq):
    up, down, left, right = flip_lr(sq)
    return rotate_90([up, down])

def filp_lr_rotate_180(sq):
    up, down, left, right = flip_lr(sq)
    return rotate_180([up, down])

def flip_lr_rotate_270(sq):
    up, down, left, right = flip_lr(sq)
    return rotate_270([up, down])


def find_next(key: int, dct: dict, limit: list, direct: str):
    curr = dct[key]
    for func1 in [
            get_edges, rotate_90, rotate_180, rotate_270, 
            flip_ud, flip_lr,
            flip_ud_rotate_90, filp_ud_rotate_180, flip_ud_rotate_270,
            flip_lr_rotate_90, filp_lr_rotate_180, flip_lr_rotate_270
        ]:
        up, down, left, right = func1(curr)
        for k in limit:
            if k in history:
                continue
            v = dct[k]
            for func2 in [
                get_edges, rotate_90, rotate_180, rotate_270, 
                flip_ud, flip_lr,
                flip_ud_rotate_90, filp_ud_rotate_180, flip_ud_rotate_270,
                flip_lr_rotate_90, filp_lr_rotate_180, flip_lr_rotate_270
            ]:
                u, d, l, r = func2(v)
                if direct == "down":
                    if down == u:
                        item = (k, func2)
                        return item
                else:
                    if right == l:
                        item = (k, func2)
                        return item
    return None

print(len(set(corners)), len(set(borders)), len(set(inners)))

size = 12
res = []
history = set()
print(find_next(3511, dct, borders, "right"))

# for first in corners:
#     history = set()
#     # build first column by first key (one of the corners)
#     col = [first]
#     history.add(first)
#     while len(col) < size - 1:
#         key = col[-1]
#         tmp = find_next(key, dct, borders, "down")
#         if not tmp:
#             break
#         key, func = tmp
#         col.append(key)
#         history.add(key)
#     if len(col) < size - 1:
#         for ck in col:
#             history.remove(ck)
#         continue
#     tmp = find_next(key, dct, corners, "down")
#     if not tmp:
#         for ck in col:
#             history.remove(ck)
#         continue
#     key, func = tmp
#     col.append(key)
#     history.add(key)

#     print("Final col: ", col)

#     # build rows by the first column
#     tmp_res = []
#     for i,col_key in enumerate(col):
#         row = [col_key]
#         history.add(col_key)
#         if i == 0 or i == size - 1:
#             edge_pool = borders
#         else:
#             edge_pool = inners
#         while len(row) < size - 1:
#             key = row[-1]
#             tmp = find_next(key, dct, edge_pool, "right")
#             if not tmp:
#                 break
#             key, func = tmp
#             row.append(key)
#             history.add(key)
#         # if len(row) < size - 1:
#         #     for rk in row:
#         #         history.remove(rk)
#         #     continue
#         if i == 0 or i == size - 1:
#             limit_pool = corners
#         else:
#             limit_pool = borders
#         key = row[-1]
#         tmp = find_next(key, dct, limit_pool, "right")
#         if not tmp:
#             for rk in row:
#                 history.remove(rk)
#             continue
#         key, func = tmp
#         row.append(key)
#         history.add(key)
#         tmp_res.append(row)

#     # print(tmp_res)
#     already_corners = set((tmp_res[0][0], tmp_res[0][-1], tmp_res[-1][0], tmp_res[-1][-1]))
#     already_borders = set(tmp_res[0][1:-1] + [i[0] for i in tmp_res[1:-1]] + [i[-1] for i in tmp_res[1:-1]] + tmp_res[-1][1:-1])
#     already_inners = set(list(chain(*tmp_res))) - already_corners - already_borders
#     print("already_corners: ", already_corners)
#     print("already_borders: ", already_borders)
#     print("already_inners: ", already_inners)
#     print(set(corners) - already_corners)
#     print(set(borders) - already_borders)
#     print(set(inners) - already_inners)
#     print()
#     res.append(tmp_res)


from pprint import pprint
pprint(res)





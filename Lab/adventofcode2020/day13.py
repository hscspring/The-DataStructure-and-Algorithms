import pnlp
import time
import copy
from functools import wraps


def timethis(func):
    @wraps(func)
    def wapper(*arg, **kwargs):
        start = time.time()
        res = func(*arg, **kwargs)
        end = time.time()
        print("cost time: ", end - start)
        return res
    return wapper


file = "data/day13.txt"
# file = "data/day13Test.txt"


lines = pnlp.read_lines(file)
ts = int(lines[0])
ids = lines[1].split(",")
ids = [int(i) if i != "x" else i for i in ids]


def get_nearest(busid: int, ts: int):
    x = 0
    while x < ts:
        x += busid
    return x


def part1(ts: int, ids: list):
    min_near = 1e100
    min_idx = 0
    for i, v in enumerate(ids):
        if v == "x":
            continue
        near = get_nearest(v, ts)
        if near < min_near:
            min_near = near
            min_idx = i
    return ids[min_idx] * (min_near - ts)


def satisfy(num: int, ids: list):
    if num % ids[0] != 0:
        return False
    for i in ids[1:]:
        num += 1
        if i == "x":
            continue
        if num % i != 0:
            return False
    return True


assert satisfy(3417, [17, "x", 13, 19]) == True
assert satisfy(754018, [67, 7, 59, 61]) == True
assert satisfy(779210, [67, "x", 7, 59, 61]) == True
assert satisfy(1261476, [67, 7, "x", 59, 61]) == True
assert satisfy(1202161486, [1789, 37, 47, 1889]) == True
assert satisfy(1068781, [7, 13, "x", "x", 59, "x", 31, 19]) == True


def get_next(first: int, last: int, i: int, length: int):
    while (first * i + length - 1) % last != 0:
        i += 1
    return i


def satisfy_given_idx(num: int, idx: int, ids: list):
    copy = num
    end = num + (len(ids) - idx - 1)
    if end % ids[0] != 0 or end % ids[-1] != 0:
        return False
    if num % ids[idx] != 0:
        return False
    for i in range(idx+1, len(ids)-1):
        v = ids[i]
        num += 1
        if v == "x":
            continue
        if num % v != 0:
            return False
    for i in range(idx-1, -1+1, -1):
        v = ids[i]
        copy -= 1
        if v == "x":
            continue
        if copy % v != 0:
            return False
    return True


assert (satisfy_given_idx(1068785, 4, [
        7, 13, 'x', 'x', 59, 'x', 31, 19])) == True


def get_max(ids):
    max_idx = -1e9
    max_val = -1e9
    for i, v in enumerate(ids):
        if v == "x":
            continue
        if v > max_val:
            max_val = v
            max_idx = i
    return max_idx, max_val


@timethis
def part2(ids, i=1):
    first = ids[0]
    # last = ids[-1]
    # length = len(ids)
    num = first
    while not satisfy(num, ids):
        i += 1
        # i = get_next(first, last, i, length)
        num = first * i
    return num


@timethis
def part2_fast(ids, i=1, min_bound=100000000000000):
    max_idx, max_val = get_max(ids)
    step = max_val
    while max_val < min_bound:
        i += 1
        max_val = step * i
    while not satisfy_given_idx(max_val, max_idx, ids):
        i += 1
        max_val = step * i
    return max_idx, max_val


# res = part1(ts, ids)
# print(res)

# res = part2(ids, 1)
# print(res)

# idx, val = part2_fast(ids, 1)
# print(val-idx)


def get_buckets(ids):
    copy_ids = copy.deepcopy(ids)
    id_pool = set()
    res = []
    while len(id_pool) < len(ids):
        idx, num = get_max(copy_ids)
        if idx == -1e9:
            break
        copy_ids[idx] = "x"
        tmp = [(idx, num)]
        id_pool.add(idx)
        for i, v in enumerate(copy_ids):
            if v == "x":
                id_pool.add(i)
                continue
            dis = abs(idx - i)
            if dis > 1 and v % dis == 0:
                tmp.append((i, v))
                copy_ids[i] = "x"
        res.append(tmp)
    return res


def combine_buckets(buckets: list):
    res = []
    for item in buckets:
        pair = item[0]
        tmp = 1
        for p in item[1:]:
            tmp *= p[1]
        new = pair[1] * tmp
        res.append((pair[0], new))
    return res


def satisfy_given_pool(num: int, max_idx: int, buckets: list):
    for (i, v) in buckets:
        if i == max_idx:
            continue
        new = num + i - max_idx
        if new % v != 0:
            return False
    return True


@timethis
def part2_faster(ids, i=1, min_bound=100000000000000):
    buckets = get_buckets(ids)
    pool = combine_buckets(buckets)
    max_idx, max_val = max(pool, key=lambda x: x[1])
    step = max_val
    while max_val < min_bound:
        i += 1
        max_val = step * i
    while not satisfy_given_pool(max_val, max_idx, pool):
        i += 1
        max_val = step * i
    return max_idx, max_val


idx, val = part2_faster(ids)
print(val-idx)  # 600689120448303

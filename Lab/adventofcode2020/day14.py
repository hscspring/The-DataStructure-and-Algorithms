import pnlp


def get_upper_bound(val: int):
    i = 0
    while 2 ** i < val:
        i += 1
    return i


def get_binary(val: int) -> str:
    res = [0] * 36
    is_odd = True
    if val % 2 == 0:
        val += 1
        is_odd = False
    while val > 1:
        bound = get_upper_bound(val)
        val -= 2 ** (bound - 1)
        res[-bound] = 1

    if is_odd:
        res[-1] = 1
    else:
        res[-1] = 0
    return res


def get_binary2(val: int) -> list:
    binary = bin(val)[2:]
    return binary.rjust(36, "0")


def get_masked_val(val: int, mask: str):
    binary = get_binary(val)
    strb = "".join(map(str, binary))
    res = [0] * 36
    for i in range(36):
        if mask[i] == "X":
            res[i] = int(strb[i])
        elif mask[i] == "1":
            res[i] = 1
        elif mask[i] == "0":
            res[i] = 0
    return res


def get_dec_val(binary: list):
    res = 0
    for i, v in enumerate(reversed(binary)):
        if v == 1:
            res += 2 ** i
    return res


def get_max():
    res = 0
    for i in range(36):
        res += 2 ** i
    return res


assert "".join(map(str, get_binary(101))
               ) == "000000000000000000000000000001100101"
assert "".join(map(str, get_binary(3))
               ) == "000000000000000000000000000000000011"
assert "".join(map(str, get_binary(4))
               ) == "000000000000000000000000000000000100"


assert get_upper_bound(3) == 2
assert get_upper_bound(9) == 4
assert get_upper_bound(101) == 7


file = "data/day14.txt"
# file = "data/day14Test2.txt"
lines = pnlp.read_lines(file)


def get_parts(lines: list):
    parts = []
    length = len(lines)
    i = 0
    while i < length:
        line = lines[i]
        part = []
        if line.startswith("mask"):
            mask = line.split(" = ")[-1]
            i += 1
        else:
            while i < length and not line.startswith("mask"):
                v1, v2 = line.split(" = ")
                loc = int(v1.replace("mem[", "").replace("]", ""))
                val = int(v2)
                part.append((loc, val))
                i += 1
                if i == length:
                    break
                line = lines[i]
            parts.append((mask, part))
    return parts


def get_sum(lines):
    parts = get_parts(lines)
    max_val = get_max()
    mem = {}
    for mask, vals in parts:
        for loc, val in vals:
            binary = get_masked_val(val, mask)
            new_val = get_dec_val(binary)
            if new_val > max_val:
                print("OVER", new_val)
            mem[loc] = new_val

    print(sum([len(vals) for mask, vals in parts]))
    print(len(mem))
    return sum(mem.values())


# res = get_sum(lines)
# print(res)


def get_masked_loc(loc: int, mask: str) -> str:
    binary = get_binary(loc)
    strb = "".join(map(str, binary))
    res = [0] * 36
    for i in range(36):
        if mask[i] == "X":
            res[i] = "X"
        elif mask[i] == "1":
            res[i] = "1"
        elif mask[i] == "0":
            res[i] = strb[i]
    return "".join(res)


def padding(lst: list, total: int):
    pad = int(total / len(lst))
    res = []
    for i in lst:
        res.extend([i] * pad)
    return res


def get_permutation(basket: list, count: int):
    init = []
    base = len(basket)
    total = base ** count
    for i in range(count):
        tmp = basket * (base**i)
        pad = padding(tmp, total)
        init.append(pad)
    res = []
    for i in range(total):
        tmp = []
        for items in init:
            tmp.append(items[i])
        res.append(tmp)
    return res


def get_actual_locs(loc: str):
    res = []
    count = loc.count("X")
    combines = get_permutation(["0", "1"], count)
    for com in combines:
        tmp = []
        i = 0
        for v in loc:
            if v == "X":
                tmp.append(com[i])
                i += 1
            else:
                tmp.append(v)
        binary = list(map(int, tmp))
        num = get_dec_val(binary)
        res.append(num)
    return res


parts = get_parts(lines)
mem = {}
for mask, vals in parts:
    for loc, val in vals:
        new_loc = get_masked_loc(loc, mask)
        actual_locs = get_actual_locs(new_loc)
        for act_loc in actual_locs:
            mem[act_loc] = val


print(sum(mem.values()))









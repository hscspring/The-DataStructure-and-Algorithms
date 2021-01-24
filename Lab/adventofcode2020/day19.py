import pnlp
import copy

file = "data/day19Test.txt"
file = "data/day19.txt"
# file = "data/day19Test2.txt"


def get_rule_msg(file):
    text = pnlp.read_file(file)
    tmp_rule, tmp_msg = text.split("\n\n")
    rule = tmp_rule.split("\n")
    msg = tmp_msg.split("\n")
    msg = [m for m in msg if m]
    return rule, msg


def build_dict(rule):
    dct = {}
    base = {}
    for line in rule:
        key, val = line.split(": ")
        if "a" in val:
            base[key] = "a"
        elif "b" in val:
            base[key] = "b"
        else:
            strs = val.split(" | ")
            dct[key] = strs
    return dct, base


def get_next(init, dct, base):
    res = []
    for item in init:
        curr_parts = item.split()
        for i, nxt_key in enumerate(curr_parts):
            if nxt_key in base:
                continue
            nxt_parts = dct[nxt_key]
            for part in nxt_parts:
                cp = copy.deepcopy(curr_parts)
                cp[i] = part
                new = " ".join(cp)
                res.append(new)
    return res


def satisfy(init, base):
    for part in init:
        if not all_base(part, base):
            return False
    return True


def all_base(item, base):
    for v in item.split():
        if v not in base:
            return False
    return True


def item2str(item, base):
    res = ""
    for key in item.split():
        val = base[key]
        res += val
    return res


def get_matched_messages(dct, base, start="0"):
    res = set()
    init = dct[start]
    while not satisfy(init, base):
        # 提前将已经完成的存好，不继续参与运算
        filted = []
        for item in init:
            if all_base(item, base):
                s = item2str(item, base)
                res.add(s)
            else:
                filted.append(item)
        init = get_next(filted, dct, base)
        init = list(set(init))
    for item in init:
        s = item2str(item, base)
        res.add(s)
    return res


rule, msg = get_rule_msg(file)
dct, base = build_dict(rule)
# matched = get_matched_messages(dct, base, "0")
# res = 0
# for line in msg:
#     if line in matched:
#         res += 1
# print(res)


################# BETTER SOLUTION #################

"""
8，重复 42
11：重复 42 和 31

raw: 42 42 31     ==> 42*(1+1) + 31*1
var1: 42 n42 n31  ==> 42*(1+n) + 31*n
var2: 42m 42 31   ==> 42*(m+1) + 31*1
var3: 42m 42n 31n ==> 42*(m+n) + 31*n
可以用来解决 part1
"""

def can_combine(prefix, set42, set31):
    n = len(list(set42)[0])
    part = len(prefix) // n
    assert len(prefix)/ n == part
    if part < 2:
        return prefix in set42

    # flag = True
    # for i in range(part):
    #     p = prefix[i*n: (i+1)*n]
    #     if p not in set42:
    #         flag = False
    #         break
    # if flag:
    #     return True

    first = prefix[:n]
    if first not in set42:
        return False
    last = prefix[-n:]
    if last not in set31:
        return False
    num42, num31 = 0, 0
    idx42, idx31 = [], []
    for i in range(part):
        p = prefix[i*n: (i+1)*n]
        if p in set42:
            num42 += 1
            idx42.append(i)
        elif p in set31:
            num31 += 1
            idx31.append(i)
        else:
            return False
    # VERTY IMPORTANT
    if not min(idx31) > max(idx42):
        return False
    if num42 - num31 < 1:
        return False
    else:
        return True


m42 = get_matched_messages(dct, base, "42")
m31 = get_matched_messages(dct, base, "31")

min_len = min(len(i) for i in msg)

res = 0
for line in msg:
    # if len(line) != min_len:
    #     continue
    if can_combine(line, m42, m31):
        res += 1
print(res)








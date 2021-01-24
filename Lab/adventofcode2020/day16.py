import pnlp


file = "data/day16Test.txt"
file = "data/day16.txt"
# file = "data/day16Test2.txt"

lines = pnlp.read_lines(file)

ids = []

for i, l in enumerate(lines):
    if l.startswith("your"):
        ids.append(i)
    elif l.startswith("nearby"):
        ids.append(i)

fields = lines[:ids[0]]
ticket = lines[ids[0]+1]
nearby = lines[ids[1]+1:]


def build_field_dict(fields):
    dct = {}
    for line in fields:
        tmp = line.split(": ")
        key = tmp[0]
        tmp2 = tmp[1].split(" or ")
        val = []
        for num in tmp2:
            tmp3 = num.split("-")
            item = (int(tmp3[0]), int(tmp3[1]))
            val.append(item)
        dct[key] = val
    return dct


def num_is_valid(num, vals: list):
    valid = False
    for val in vals:
        start, end = val
        if start <= num <= end:
            valid = True
            break
    return valid


def is_valid(nums: list):
    res = {}
    for key in field_dict:
        vals = field_dict[key]

        for num in nums:
            if num_is_valid(num, vals):
                if num in res:
                    res[num].append(key)
                else:
                    res[num] = [key]
    valid = True
    val = -1
    for num in nums:
        if num not in res:
            valid = False
            val = num
            break
    return valid, val


field_dict = build_field_dict(fields)


def part1(nearby):
    res = 0
    for ticket in nearby:
        valid, val = is_valid(ticket)
        if valid:
            res += val
    return res

# res = part1(nearby)
# print(res)


def filter_valid(nearby):
    new = []
    for tic in nearby:
        nums = list(map(int, tic.split(",")))
        valid, val = is_valid(nums)
        if valid:
            new.append(nums)
    return new


def get_cols_from_nearby(nearby):
    res = []
    for i in range(len(nearby[0])):
        res.append([])
    for tic in nearby:
        for i in range(len(tic)):
            res[i].append(tic[i])
    return res


def get_match_dict(cols):
    res = {}
    for i, col in enumerate(cols):
        for key in field_dict:
            standards = field_dict[key]
            flag = True
            for num in col:
                if not num_is_valid(num, standards):
                    flag = False
                    break
            if flag:
                if key in res:
                    res[key].append(i)
                else:
                    res[key] = [i]
    return (res)


def some_key_have_more_than_two(dct):
    flag = False
    for key in dct:
        lst = dct[key]
        if len(lst) > 0:
            flag = True
            break
    return flag


def get_filed_index_dict(match_dict: dict):
    id_dict = set(range(len(match_dict)))
    field_index = {}
    while some_key_have_more_than_two(match_dict):
        for key in match_dict:
            lst = match_dict[key]
            if len(lst) == 0:
                continue
            if len(lst) == 1:
                val = lst[0]
                field_index[key] = val
                id_dict.remove(lst[0])
                for key2 in match_dict:
                    lst2 = match_dict[key2]
                    if val in lst2:
                        lst2.remove(val)
                continue
            else:
                lst = set(lst) & id_dict
    return field_index


new_nearby = filter_valid(nearby)
cols = get_cols_from_nearby(new_nearby)
match_dict = get_match_dict(cols)
filed_index_dict = get_filed_index_dict(match_dict)

my_ticket = list(map(int, ticket.split(",")))
res = 1
for key in filed_index_dict:
    idx = filed_index_dict[key]
    if key.startswith("departure"):
        res *= my_ticket[idx]
print(res)

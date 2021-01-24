import pnlp

file = "day7Test.txt"
# file = "day7Test2.txt"

file = "day7.txt"

query = "shiny gold"

def get_bag_colors(file, query):
    lines = pnlp.read_lines(file)
    dct = {}
    for line in lines:
        tmp = line.split(" bags contain ")
        val = tmp[0]
        if not val:
            continue
        keys = tmp[1].split(" bag")
        for key in keys:
            key = " ".join(key.split()[-2:])
            if " " not in key:
                continue
            if key in dct:
                dct[key].append(val)
            else:
                dct[key] = [val]

    res = set()
    stack = [query]
    while stack:
        q = stack.pop(0)
        for adj in dct.get(q, []):
            stack.append(adj)
            res.add(adj)

    return len(res)


# res = get_bag_colors(file, query)
# print(res)


lines = pnlp.read_lines(file)
dct = {}
for line in lines:
    tmp = line.split(" bags contain ")
    key = tmp[0]
    if not key:
        continue
    vals = tmp[1].split(" bag")
    pairs = []
    for val in vals:
        tmp2 = val.split()        
        if len(tmp2) < 3:
            continue
        color = " ".join(tmp2[-2:])
        num = int(tmp2[-3])
        pairs.append((color, num))
    if key in dct:
        dct[key].extend(pairs)
    else:
        dct[key] = pairs


res = 0
stack = [(query, 1)]
while stack:
    q, n = stack.pop(0)
    for adj in dct.get(q, []):
        newn = adj[1]*n
        res += newn
        new = (adj[0], newn)
        stack.append(new)
        
print(res)



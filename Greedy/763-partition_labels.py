from collections import Counter



def partition_labels(s: str) -> list:
    res = []
    count = Counter(s)
    addr = {}
    for i,c in enumerate(s):
        if c in addr:
            addr[c].append(i)
        else:
            addr[c] = [i]
    
    lst = []
    added = set()
    for c in s:
        if c in added:
            continue
        loc = addr[c]
        item = (c, loc[0], loc[-1])
        lst.append(item)
        added.add(c)

    total = count[lst[0][0]]
    prev = lst[0][2]
    for i in range(1, len(lst)):
        item = lst[i]
        if item[1] < prev:
            total += count[item[0]]
            if item[2] > prev:
                prev = item[2]
        else:
            res.append(total)
            total = count[item[0]]
            prev = item[2]
    res.append(total)
    return res


def standard_solution(s: str) -> list:
    res = []
    last = {c:i for i,c in enumerate(s)}
    j = anchor = 0
    for i,c in enumerate(s):
        j = max(j, last[c])
        if i == j:
            res.append(i - anchor + 1)
            anchor = i + 1
    return res


s = "ababcbacadefegdehijhklij"
res = partition_labels(s)
print(res)


res = standard_solution(s)
print(res)


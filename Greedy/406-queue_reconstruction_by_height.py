

people = [[7,1],[7,0],[4,4],[6,1],[5,2],[5,0]]

# [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]

def func(people):
    peopledct = {}
    for i in range(len(people)):
        p = people[i]
        if p[0] in peopledct:
            peopledct[p[0]].append((p[1], i))
        else:
            peopledct[p[0]] = [(p[1], i)]
    
    sort = sorted(peopledct, reverse=True)
    res = []
    for h in sort:
        for p in sorted(peopledct[h]):
            res.insert(p[0], people[p[1]])
    return res


res = func(people)
print(res)
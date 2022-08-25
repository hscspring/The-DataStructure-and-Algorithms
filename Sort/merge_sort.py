def merge_sort(lst: list) -> list:

    def merge(l: list, r: list) -> list:
        while l and r:
            if l[0] > r[0]:
                yield r.pop(0)
            else:
                yield l.pop(0)
        if l:   
            yield from l
        if r:
            yield from r

    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    return list(merge(merge_sort(lst[:mid]), merge_sort(lst[mid:])))


lst = [1,2,3,3,3,3,3,4,5,3,3,2,1]
res = merge_sort(lst)
print(res)

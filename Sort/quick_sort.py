def quick_sort(lst: list) -> list:
    if len(lst) < 2:
        return lst
    l, m, r = [], [], []
    pivot = lst[0]
    for i in lst:
        if i > pivot:
            r.append(i)
        elif i < pivot:
            l.append(i)
        else:
            m.append(i)
    return quick_sort(l) + m + quick_sort(r)


lst = [1,2,3,3,3,3,3,4,5,3,3,2,1]
res = quick_sort(lst)
print(res)


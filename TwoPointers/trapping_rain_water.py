def fuck_onn(arr):
    res = 0
    for i in range(1, len(arr)):
        v = arr[i]
        minh = min(max(arr[:i]), max(arr[i:]))
        x = minh - v
        if x > 0:
            res += x
    return res


def fuck_on(arr):
    lm = arr[0]
    lms = []
    for v in arr:
        lm = max(lm, v)
        lms.append(lm)

    res = 0
    e = arr[-1]
    for i in range(len(arr) - 1, -1, -1):
        e = max(arr[i], e)
        s = min(e, lms[i])
        res += (s - arr[i])
    return res


arr = [3, 1, 2, 5, 2, 4]
res1 = fuck_onn(arr)
res2 = fuck_on(arr)
print(res1, res2)

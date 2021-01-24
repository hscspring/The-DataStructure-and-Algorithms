from functools import wraps
import time


def timethis(func):
    @wraps(func)
    def warpper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print("Cost time: ", end - start)
        return res
    return warpper


s = "0,3,6"
s = "20,0,1,11,6,3"


@timethis
def get_nth(s: str, total: int):
    nums = list(map(int, s.split(",")))
    nums.append(0)
    i = len(nums)

    def get_idx(num, idx):
        while idx >= 0 and nums[idx] != num:
            idx -= 1
        return idx

    while i < total:
        curr = nums[i-1]
        if curr in nums[:i-1]:
            idx = get_idx(curr, i-2)
            x = i - (idx + 1)
        else:
            x = 0
        nums.append(x)
        i += 1
    return nums[-1]


@timethis
def get_nth2(s: str, total: int):
    nums = list(map(int, s.split(",")))
    i = len(nums)
    rg = range(i)
    dct = dict(zip(rg, nums))
    history = dict(zip(nums, rg))
    dct[i] = 0
    while i < total:
        val = dct[i-1]
        if val in history:
            idx = history[val]
            x = i - 1 - idx
        else:
            x = 0
        history[val] = i - 1
        dct[i] = x
        i += 1
    return (list(dct.values())[-1])


total = 2020
assert get_nth("0,3,6", total) == 436
assert get_nth("1,3,2", total) == 1
assert get_nth("2,1,3", total) == 10
assert get_nth("1,2,3", total) == 27
assert get_nth("2,3,1", total) == 78
assert get_nth("3,2,1", total) == 438
assert get_nth("3,1,2", total) == 1836

assert get_nth2("0,3,6", total) == 436
assert get_nth2("1,3,2", total) == 1
assert get_nth2("2,1,3", total) == 10
assert get_nth2("1,2,3", total) == 27
assert get_nth2("2,3,1", total) == 78
assert get_nth2("3,2,1", total) == 438
assert get_nth2("3,1,2", total) == 1836

# total = 30000000
# assert get_nth2("1,3,2", total) == 2578
# assert get_nth2("2,1,3", total) == 3544142
# assert get_nth2("1,2,3", total) == 261214
# assert get_nth2("2,3,1", total) == 6895259
# assert get_nth2("3,2,1", total) == 18
# assert get_nth2("3,1,2", total) == 362


total = 2020
res = get_nth(s, total)
print(res)

total = 30000000
res = get_nth2(s, total)
print(res) # 24s

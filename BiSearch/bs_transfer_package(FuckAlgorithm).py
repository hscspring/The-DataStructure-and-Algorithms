"""
传送带第 i 个包裹重量为 weights[i]，每一天都会按给出重量的顺序往传送带上放包裹，装载的重量不会超过传送带的最大运载重量。
返回能在 D 天内将传送带上所有包裹送达的最低运载能力。

Input: weights = [1,2,3,4,5,6,7,8,9,10], D = 5
Output: 15

注意：
是按照给定的重量顺序，不能随意调整顺序；可能有序也可能无序
货物不可分割

"""


def bisearch(weights: list, day: int) -> int:
    min_catacity = max(weights)
    max_catacity = sum(weights)
    while min_catacity < max_catacity:
        mid = (min_catacity + max_catacity) // 2
        if can_finish(weights, day, mid):
            max_catacity = mid
        else:
            min_catacity = mid + 1
    return min_catacity

def can_finish(weights: list, day: int, capacity: int) -> bool:
    i = 0
    for _ in range(day):
        tmp = 0
        while tmp < capacity: # and i < len(weights):
            tmp += weights[i]
            i += 1
            if tmp > capacity:
                i -= 1
            if i == len(weights):
                return True
    return False


def can_finish2(weights: list, day: int, capacity: int) -> bool:
    i = 0
    for _ in range(day):
        tmp = capacity
        while (tmp - weights[i]) >= 0:
            tmp -= weights[i]
            i += 1
            if i == len(weights):
                return True
    return False

for i in range(10, 16):
    print(can_finish([1,2,3,4,5,6,7,8,9,10], 5, i))
    print(can_finish2([1,2,3,4,5,6,7,8,9,10], 5, i))

assert bisearch([1,2,3,4,5,6,7,8,9,10], 5) == 15
assert bisearch([7,8,1,2], 3) == 8
assert bisearch([7,8,1,2], 1) == 18
assert bisearch([7,8,1,2], 10) == 8
assert bisearch([5], 3) == 5
assert bisearch([5], 6) == 5

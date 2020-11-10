#   // You have an array with 0 or 1. 
#   // 0 represents empty space and 1 represents wall. 
#   // for example 
#   // [0 0 0 1 0 0 0 1 0 0 0 1 0 1] 
#   // Compute an output vector, in which each element represents 
#   // the distance to the closest wall. 
#   // for example, the output of the above vector should be 
#   // [3 2 1 0 1 2 1 0 1 2 1 0 1 0]

def get_distance_to_the_closet_wall1(lst: list) -> list:
    if not lst:
        return []
    result = []
    length = len(lst)
    for i in range(length):
        if lst[i] == 1:
            result.append(0)
            continue
        left, right = i, i
        while left > 1 or right < length - 1:
            if ((left > 0 and lst[left-1] == 1) or
                        (right < length-1 and lst[right+1] == 1)
                    ):
                break
            else:
                left -= 1
                right += 1
        if left > 0 and lst[left-1] == 1:
            result.append(abs(left-i)+1)
        elif right < length-1 and lst[right+1] == 1:
            result.append(abs(right-i)+1)
        else:
            result.append(0)
    return result


def get_sub_distance(sub_s, is_start: bool, is_end: bool):
    if is_start:
        return list(range(len(sub_s), 0, -1))
    elif is_end:
        return list(range(1, len(sub_s)+1))
    else:
        mid = len(sub_s) // 2
        left = list(range(1, mid+1))
        right = list(reversed(left))
        if len(sub_s) % 2 == 0:
            return left + right
        else:
            return left + [mid+1] + right


def get_distance_to_the_closet_wall2(lst: list) -> list:
    if not lst:
        return []
    result = []
    s = "".join(list(map(str, lst)))
    parts = s.split("1")
    length = len(parts)
    if length == 1:
        return lst
    for i, part in enumerate(parts):
        if i == 0:
            sub = get_sub_distance(part, True, False)
        elif i == length - 1:
            sub = get_sub_distance(part, False, True)
        else:
            sub = get_sub_distance(part, False, False)
        result.extend(sub)
        result.append(0)
    return result[:-1]


for get_distance_to_the_closet_wall in [
        get_distance_to_the_closet_wall1, get_distance_to_the_closet_wall2]:

    lst = [0, 0, 1]
    assert get_distance_to_the_closet_wall(lst) == [2, 1, 0]

    lst = [0, 1, 0]
    assert get_distance_to_the_closet_wall(lst) == [1, 0, 1]

    lst = [1, 0, 0]
    assert get_distance_to_the_closet_wall(lst) == [0, 1, 2]

    lst = [0, 0, 0]
    assert get_distance_to_the_closet_wall(lst) == [0, 0, 0]

    lst = [1, 1, 1]
    assert get_distance_to_the_closet_wall(lst) == [0, 0, 0]

    lst = [1, 0, 1]
    assert get_distance_to_the_closet_wall(lst) == [0, 1, 0]

    lst = [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1]
    ret = [3, 2, 1, 0, 1, 2, 1, 0, 1, 2, 1, 0, 1, 0]
    assert get_distance_to_the_closet_wall(lst) == ret

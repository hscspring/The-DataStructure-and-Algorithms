import pnlp

lines = pnlp.read_lines("day2.txt")


def is_valid(line: str):
    num, key, txt = line.strip().split()
    s, e = list(map(int, num.split("-")))
    key = key[0]
    if s <= txt.count(key) <= e:
        return True
    return False

assert is_valid("1-3 a: abcde") == True
assert is_valid("1-3 b: cdefg") == False
assert is_valid("2-9 c: ccccccccc") == True


res = [is_valid(line) for line in lines]

print(res.count(True))


def is_valid_another(line: str):
    num, key, txt = line.strip().split()
    s, e = list(map(int, num.split("-")))
    key = key[0]
    s = s-1
    e = e-1
    if txt[s] == key and txt[e] == key:
        return False
    if txt[s] == key or txt[e] == key:
        return True
    return False

assert is_valid_another("1-3 a: abcde") == True
assert is_valid_another("1-3 b: cdefg") == False
assert is_valid_another("2-9 c: ccccccccc") == False

res = [is_valid_another(line) for line in lines]

print(res.count(True))
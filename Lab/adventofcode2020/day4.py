import pnlp


needs = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
colors = set("a b c d e f 0 1 2 3 4 5 6 7 8 9".split())
eye_colors = set("amb blu brn gry grn hzl oth".split())
nums = set("0 1 2 3 4 5 6 7 8 9".split())

def valid_num(val: str, low: int, high: int) -> bool:
        try:
            num = int(val)
        except Exception as e:
            return False
        return low <= num <= high

class Validator:

    valid_byr = lambda x: valid_num(x, 1920, 2002)
    valid_iyr = lambda x: valid_num(x, 2010, 2020)
    valid_eyr = lambda x: valid_num(x, 2020, 2030)

    def valid_hgt(val: str) -> bool:
        unit = val[-2:]
        if unit not in ["cm", "in"]:
            return False
        try:
            num = int(val[:-2])
        except Exception as e:
            return False
        if unit == "cm":
            return 150 <= num <= 193
        else:
            return 59 <= num <= 76

    def valid_hcl(val: str) -> bool:
        if not val.startswith("#"):
            return False
        if len(val) != 7:
            return False
        for v in val[1:]:
            if v not in colors:
                return False
        return True

    def valid_ecl(val: str) -> bool:
        return val in eye_colors

    def valid_pid(val: str) -> bool:
        if len(val) != 9:
            return False
        for v in val:
            if v not in nums:
                return False
        return True


def count_valid(file):
    file = pnlp.read_file(file)

    ps = file.split("\n\n")
    res = 0
    for p in ps:
        pd = {}
        for line in p.split("\n"):
            for item in line.strip().split():
                tmp = item.split(":")
                key = tmp[0]
                val = tmp[1]
                if key == "cid":
                    continue
                pd[key] = val
        if needs - set(pd.keys()) == set():
            is_valid = True
            for key,val in pd.items():
                func = getattr(Validator, "valid_" + key)
                if not func(val):
                    is_valid = False
                    break
            if is_valid:
                res += 1
    return res


res = count_valid("day4Test2.txt")
print(res)

res = count_valid("day4.txt")
print(res)
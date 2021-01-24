import pnlp


file = "day6Test.txt"
file = "day6.txt"


def get_count1(file):
    text = pnlp.read_file(file)
    parts = text.split("\n\n")
    res = 0
    for part in parts:
        tmp = set()
        for line in part.split("\n"):
            for a in line:
                tmp.add(a)
        res += len(tmp)

    return (res)



text = pnlp.read_file(file)
parts = text.split("\n\n")

res = 0

for part in parts:
    lines = part.split("\n")
    len_lines = len(lines)
    tmp = {}
    for line in lines:
        for a in line:
            if a in tmp:
                tmp[a] += 1
            else:
                tmp[a] = 1
    for key,val in tmp.items():
        if val >= len_lines:
            res += 1
print(res)


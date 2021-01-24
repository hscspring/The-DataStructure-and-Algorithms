import pnlp



def get_one_three_nums(lines):
    max_val = max(lines)
    highest = max_val + 3
    sort = sorted(lines, reverse=True)
    dct = {1: 0, 2: 0, 3: 0}
    curr = highest
    for i in sort:
        key = curr - i
        dct[key] += 1
        curr = i
    if sort[-1] in dct:
        dct[sort[-1]] += 1
    return (dct[1] * dct[3])


file = "day10Test.txt"
# file = "day10Test2.txt"
file = "day10.txt"

lines = pnlp.read_lines(file)
lines = list(map(int, lines))
res = get_one_three_nums(lines)


n = 1
sort = sorted(lines, reverse=True)

slide = []
if sort[-1] > 0:
    sort.append(0)

length = len(sort)
diff = []
for i in range(length-1):
    diff.append(sort[i]-sort[i+1])

i = 0
while i < length-1:
    num = 0
    if diff[i] != 1:
        i += 1
        continue
    while i < length-1 and diff[i] == 1:
        i += 1
        num += 1
    if num == 2:
        n *= 2
    elif num == 3:
        n *= 4
    elif num == 4:
        n *= 7

print(n)


import pnlp


def get_tree_num(file, right: int, down: int):
    data = []
    row, col = 0, 0
    lines = pnlp.read_lines(file)
    for line in lines:
        line = line.strip()
        data.append(list(line))
    
    rows = len(data)
    cols = len(data[0])

    res = []
    num = 0

    while row < rows - down:
        col += right
        row += down

        val = data[row][col%cols]
        if val == "#":
            num += 1
        res.append(val)
    return num


prod = 1
prod2 = 1
for (right, down) in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
    res = get_tree_num("day3Test.txt", right, down)
    prod *= res
    res2 = get_tree_num("day3.txt", right, down)
    prod2 *= res2
print(prod)
print(prod2)

def read_file(fp):
    with open(fp, "r") as f:
        data = f.read().split("\n")
    return data

def pad_data(data_list):
    lst = []
    lenth = 0
    for item in data_list:
        sub = item.split(",")
        lst.append(sub)
        if len(sub) > lenth:
            lenth = len(sub)
    for i in range(len(lst)):
        item = lst[i]
        for j in range(len(item)):
            if i > 0 and item[j] == "":
                item[j] = lst[i-1][j]
        if len(item) < lenth:
            item.extend([""] * (lenth - len(item)))
    return lst

def build_tree(data_list):
    tree = {}
    rows = len(data_list)
    cols = len(data_list[0])
    for i in range(rows):
        sub = tree
        for j in range(cols):
            val = data_list[i][j]

            if val != "":
                if val not in sub:
                    if j < cols-1:
                        sub[val] = [{}]
                    else:
                        sub[val] = []
                if len(sub[val]) > 0:
                    sub = sub[val][0]
    return tree

def find(tree, key):
    def _find_core(tree, key, res):
        found = False
        for i in tree:
            if key not in res:
                res.append(i)
            if i == key:
                return True
            if not found: # and len(tree[i]) > 0:
                for j in tree[i]:
                    found = _find_core(j, key, res)
            if not found:
                res.pop()
        return found
    res = []
    _find_core(tree, key, res)
    if len(res) == 0:
        return "not found"
    else:
        return ".".join(res)
    

path = "data.txt"
dl = read_file(path)
pdl = pad_data(dl)
tree = build_tree(pdl)
print(tree)
res = find(tree, "种姓制度")
print(res)


from pprint import pprint

def read_file(fp):
    with open(fp, "r") as f:
        data = f.read().split("\n")
    return data

def pad_data(data_list):
    lst = []
    for item in data_list:
        lst.append(item.split(","))
    for i in range(len(lst)):
        item = lst[i]
        for j in range(len(item)):
            if i > 0 and item[j] == "":
                item[j] = lst[i-1][j]
    return lst

def construct(data):
    root = data[0][0]
    res = [{"loc": root, "parent": ".", "children": []}]
    for item in data:
        loc = ".".join(item)
        parent = ".".join(item[:-1])
        res.append({"loc": loc, "parent": parent, "children": []})
    return sorted(res, key=lambda x: len(x["loc"].split(".")), reverse=True)

def build_tree(lst):
    root = {}
    for item in lst:
        item["children"] = root.get(item["loc"], [])
        root.update({item["parent"]: [item] + root.get(item["parent"], [])})
    return root

def dft(tree, key):
    stack = [tree]
    while stack:
        curr = stack.pop()
        loc = curr["loc"]
        if key == loc.split(".")[-1]:
            return loc
        stack.extend(reversed(curr["children"]))
    return "not found"

path = "data.txt"
dl = read_file(path)
pdl = pad_data(dl)
cdl = construct(pdl)
pprint(cdl)
print()
tree = build_tree(cdl)["."][0]
pprint(tree)
res = dft(tree, "种姓制度")
print(res)


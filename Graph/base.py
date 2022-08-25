

# 二叉树
def traverse_binary_tree(root):
    if not root:
        return
    traverse_binary_tree(root.left)
    traverse_binary_tree(root.right)


# 多叉树
def traverse_multiway_tree(root):
    if not root:
        return
    for child in root.children:
        traverse_multiway_tree(child)


# 图
def traverse_graph(graph, idx):
    visited = []
    if visited[idx]:
        return
    visited[idx] = True
    for neighbor in graph.neighbors(idx):
        traverse_graph(graph, neighbor)

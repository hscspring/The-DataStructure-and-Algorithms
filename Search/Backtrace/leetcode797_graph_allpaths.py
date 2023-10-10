"""
给你一个有 n 个节点的 有向无环图（DAG），请你找出所有从节点 0 到节点 n-1 的路径并输出（不要求按特定顺序）

 graph[i] 是一个从节点 i 可以访问的所有节点的列表（即从节点 i 到节点 graph[i][j] 存在一条有向边）。


输入：graph = [[1,2],[3],[3],[]]
输出：[[0,1,3],[0,2,3]]

"""


def dfs(graph, start, end):
    stack = [(start, [start])]
    visited = set()
    while stack:
        curr, path = stack.pop()
        if curr == end:
            return path
        for v in graph[curr]:
            if v not in visited:
                stack.append((v, path + [v]))
                visited.add(v)
    return []


def run1(graph):
    g = {}
    for i in range(len(graph)):
        g[i] = graph[i]
    res = dfs(g, 0, len(graph) - 1)
    return res


def run2(graph):
    res = []
    path = []

    def func(node, end):
        path.append(node)
        if node == end:
            res.append(path.copy())
        for v in graph[node]:
            # 不走回头路
            if v not in path:
                func(v, end)
        path.pop()

    func(0, len(graph) - 1)
    return res


inp = [[1, 2], [3], [3], []]
res1 = run1(inp)
print(res1)

res2 = run2(inp)
print(res2)

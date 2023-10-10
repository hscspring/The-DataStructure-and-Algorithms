

from collections import defaultdict


def unique_path(m, n):
    """
    # 求路径
    一个机器人在 m×n 大小的地图的左上角（起点）。
    机器人每次可以向下或向右移动。机器人要到达地图的右下角（终点）。
    可以有多少种不同的路径从起点走到终点？
    """
    dp = [[0] * (n) for i in range(m)]
    for i in range(m):
        dp[i][0] = 1
    for i in range(n):
        dp[0][i] = 1
    for i in range(m):
        for j in range(n):
            dp[i][j] = dp[i - 1][j] + dp[i][j + 1]
    return dp[-1][-1]


# 所有路径数量
def all_paths(graph, start, end):
    n = len(graph)
    dp = [0] * n
    dp[end] = 1  # 终点到自己路径数量为1
    for u in range(n - 1, -1, -1):
        for v in graph[u]:
            dp[u] += dp[v]
    print(dp)
    return dp[start]


inp = [[1, 2], [2, 3], [4], [4], []]
res = all_paths(inp, 0, 4)
print("所有路径数量：", res)


# 最短路径长度(最好先拓扑排序)
def shortest_path_len(adj_list, start, end):
    n = len(adj_list)
    dp = [1e5] * n
    dp[start] = 0

    for u in range(n):
        for v in adj_list[u]:
            if dp[u] + 1 < dp[v]:
                dp[v] = dp[u] + 1
        if end == u:
            break
    print(dp)
    return dp[end]


res = shortest_path_len(inp, 0, 4)
print("最短路径的长度：", res)


# 最短路径（最好先拓扑排序）
def shortest_path(adj_list, start, end):
    n = len(adj_list)
    dp = [1e5] * n
    dp[start] = 0
    parent = [-1] * n

    for u in range(n):
        for v in adj_list[u]:
            if dp[u] + 1 < dp[v]:
                dp[v] = dp[u] + 1
                parent[v] = u
        if end == u:
            break
    path = []
    curr = end
    while curr != -1:
        path.insert(0, curr)
        curr = parent[curr]
    print(dp)
    return path


res = shortest_path(inp, 0, 4)
print("最短路径：", res)


def topological_sort(graph):
    # 入度
    in_degree = defaultdict(int)
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    # 根节点
    queue = [node for node in graph if in_degree[node] == 0]
    topo_order = []

    while queue:
        node = queue.pop(0)
        topo_order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            # 入度为0，则添加到队列，作为拓扑排序下个节点
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return topo_order


graph = {0: [1, 2], 1: [2, 3], 2: [4], 3: [4], 4: []}
res = topological_sort(graph)
print("拓扑排序：", res)

inp = [[1, 2], [2, 3], [4], [4], []]

#

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
    # print("\t dp: ", dp)
    return dp[end]


# 最短路径（最好先拓扑排序）
def shortest_path_dp(adj_list, start, end):
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
    # print("\t dp: ", dp)
    return path


def shortest_path_bfs(adj_list, start, end):
    path = [start]
    q = [(start, path)]
    while q:
        u, path = q.pop(0)
        if u == end:
            return path
        else:
            for v in adj_list[u]:
                # 不走回头路
                if v not in path:
                    q.append((v, path + [v]))
    return path


res = shortest_path_len(inp, 0, 4)
print("最短路径的长度：", res)
res = shortest_path_dp(inp, 0, 4)
print("DP最短路径：", res)
res = shortest_path_bfs(inp, 0, 4)
print("BFS最短路径：", res)

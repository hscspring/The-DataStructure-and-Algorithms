"""
vivo 游戏中心的运营小伙伴最近接到一款新游戏的上架申请，为了保障用户体验，运营同学将按运营流程和规范对其做出分析评估。经过初步了解后分析得知，该游戏的地图可以用一个大小为 n*n 的矩阵表示，每个元素可以视为一个格子，根据游戏剧情设定其中某些格子是不可达的 (比如建筑、高山、河流或者其它障碍物等)，现在请你设计一种算法寻找从起点出发到达终点的最优抵达路径，以协助运营小伙伴评估该游戏的可玩性和上手难度。

第一行表示矩阵大小 n，5
第二行表示起点和终点的坐标
第三行起是一个用矩阵表示的游戏地图，其中#或者@表示障碍物，其他字母、非0数字、以及符号+、-、* 等等均表示普通可达格子，共有 n 行  n 列


输入例子：
15
0 7 7 7
*5#++B+B+++++$3
55#+++++++###$$
###$++++++#+*#+
++$@$+++$$$3+#+
+++$$+++$+4###+
A++++###$@+$++A
+++++#++$#$$+++
A++++#+5+#+++++
+++$$#$++#++++A
+++$+@$###+++++
+###4+$+++$$+++
+#+3$$$+++$##++
+#*+#++++++#$$+
$####+++++++$##
3$+++B++B++++#5
"""


def dfs(x, y, ex, ey, m, visited, count):
    if x < 0 or y < 0 or x >= len(m) or y >= len(m[0]) or m[x][y] in "#@":
        return
    if visited[x][y] == 0 or visited[x][y] > count:
        visited[x][y] = count
        if x == ex and y == ey:
            return
        dfs(x, y + 1, ex, ey, m, visited, count + 1)
        dfs(x, y - 1, ex, ey, m, visited, count + 1)
        dfs(x + 1, y, ex, ey, m, visited, count + 1)
        dfs(x - 1, y, ex, ey, m, visited, count + 1)


def bfs(x, y, ex, ey, m, visited):
    q = [(x, y)]
    visited[x][y] = 1
    directs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    lenx = len(m)
    leny = len(m[0])
    count = 0
    while q:
        length = len(q)
        for i in range(length):
            curr = q.pop(0)
            if curr[0] == ex and curr[1] == ey:
                return count
            for mx, my in directs:
                nx = curr[0] + mx
                ny = curr[1] + my
                if nx >= 0 and nx < lenx and ny >= 0 and ny < leny and m[
                        nx][ny] not in "#@" and visited[nx][ny] == 0:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
        count += 1
    return -1


n = 15
sx, sy = 7, 0
ex, ey = 7, 7
ms = """*5#++B+B+++++$3
55#+++++++###$$
###$++++++#+*#+
++$@$+++$$$3+#+
+++$$+++$+4###+
A++++###$@+$++A
+++++#++$#$$+++
A++++#+5+#+++++
+++$$#$++#++++A
+++$+@$###+++++
+###4+$+++$$+++
+#+3$$$+++$##++
+#*+#++++++#$$+
$####+++++++$##
3$+++B++B++++#5"""
m = ms.split("\n")

print(m)

visited = [[0] * n for _ in range(n)]
dfs(sx, sy, ex, ey, m, visited, 1)
print(visited)
print(visited[ex][ey] - 1)

visited = [[0] * n for _ in range(n)]
res = bfs(sx, sy, ex, ey, m, visited)
print(visited)
print(res)

"""

面试题 47：礼物的最大价值
题目：在一个 m×n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值
（价值大于 0）。你可以从棋盘的左上角开始拿格子里的礼物，并每次向左或
者向下移动一格直到到达棋盘的右下角。给定一个棋盘及其上面的礼物，请计
算你最多能拿到多少价值的礼物？
"""



def get_max_value1(matrix: list) -> int:
    """
    

    Parameters
    -----------

    Returns
    ---------


    Notes
    ------

    """
    if not matrix or not matrix[0]:
        return 0
    rows, cols = len(matrix), len(matrix[0])
    res = []
    for i in range(rows):
        tmp = []
        for j in range(cols):
            tmp.append(0)
        res.append(tmp)

    for i in range(rows):
        for j in range(cols):
            up, left = 0, 0
            if i > 0:
                up = res[i-1][j]
            if j > 0:
                left = res[i][j-1]
            res[i][j] = max(up, left) + matrix[i][j]
    return res[-1][-1]


def get_max_value2(matrix: list) -> int:
    if not matrix or not matrix[0]:
        return 0
    rows, cols = len(matrix), len(matrix[0])
    res = [0] * cols
    for i in range(rows):
        for j in range(cols):
            up, left = 0, 0
            if i > 0:
                up = res[j]
            if j > 0:
                left = res[j-1]
            res[j] = max(up, left) + matrix[i][j]
    return res[-1]





if __name__ == '__main__':
    matrix = [[1,10,3,8],[12,2,9,6],[5,7,4,11]]
    res = get_max_value2(matrix)
    print(res)













    
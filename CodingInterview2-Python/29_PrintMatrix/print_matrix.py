"""
面试题 29：顺时针打印矩阵
题目：输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。

"""


def make_matrix(rows: int, cols: int) -> list:
    res = []
    k = 0
    for i in range(rows):
        tmp = []
        for j in range(cols):
            k += 1
            tmp.append(k)
        res.append(tmp)
    return res


def print_matrix_clockwisely(matrix: list) -> list:
    """
    Print the given matrix clockwesely.

    Parameters
    -----------
    matrix: list[list]
        the given matrix.

    Returns
    ---------
    out: list
        the clockwise order of the matrix.

    Notes
    ------

    """
    if not matrix:
        return []
    if not matrix[0]:
        return []
    res = []
    start = 0
    rows, cols = len(matrix), len(matrix[0])
    while rows > 2 * start and cols > 2 * start:
        print_circle(matrix, rows, cols, start, res)
        start += 1
    return res


def print_circle(matrix: list, rows: int, cols: int, start: int, res: list):
    endx = cols - 1 - start
    endy = rows - 1 - start
    # left -> right
    for i in range(start, endx+1):
        res.append(matrix[start][i])
    # up -> below
    if start < endy:
        for i in range(start+1, endy+1):
            res.append(matrix[i][endx])
    # right -> left
    if start < endx and start < endy:
        for i in reversed(range(start, endx)):
            res.append(matrix[endy][i])
    # below -> up
    if start < endx and start < endy - 1:
        for i in reversed(range(start+1, endy)):
            res.append(matrix[i][start])


if __name__ == '__main__':
    m = make_matrix(1,5)
    print(m)
    res = print_matrix_clockwisely(m)
    print(res)








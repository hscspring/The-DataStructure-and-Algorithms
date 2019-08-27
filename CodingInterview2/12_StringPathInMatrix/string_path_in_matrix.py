"""
面试题 12：矩阵中的路径
题目：请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有
字符的路径。路径可以从矩阵中任意一格开始，每一步可以在矩阵中向左、右、
上、下移动一格。如果一条路径经过了矩阵的某一格，那么该路径不能再次进入
该格子。例如在下面的 3×4 的矩阵中包含一条字符串 “bfce” 的路径（路径中的字
母用下划线标出）。但矩阵中不包含字符串 “abfb” 的路径，因为字符串的第一个
字符 b 占据了矩阵中的第一行第二个格子之后，路径不能再次进入这个格子。
A B T G
C F C S
J D E H

"""


def has_path(matrix, path: str) -> bool:
    """
    Given a matrix, make sure there is a path for a given string or not.

    Parameters
    ----------
    path: str
        A given path, like "abcd"

    Returns
    -------
    out: bool
        Whether the given path can be found in the matrix

    """
    if not path:
        return True
    if not matrix[0]:
        return False
    rows, cols = len(matrix), len(matrix[0])
    visited = []
    for i in range(rows):
        tmp = []
        for j in range(cols):
            tmp.append(False)
        visited.append(tmp)
    plen = 0
    for row in range(rows):
        for col in range(cols):
            hasp = has_path_core(matrix, row, col, rows, cols,
                                 path, plen, visited)
            if hasp:
                return True
    return False


def has_path_core(matrix, row, col, rows, cols,
                  string, plen, visited) -> bool:
    """
    When string[plen] == matrix[row][col], we could find whether
    string[plen+1] is in the surroundings of matrix[row][col].

    If not, go back to the string[plen-1]

    Notes
    ------
    The key points are as belows:
    - True: plen == len(string)
    - when matrix[row][col] == string[plen], find next
    - not visited[row][col] for each round
    - if not hasp, back
    """
    if plen == len(string):
        return True
    hasp = False
    if (row >= 0 and col >= 0 and row < rows and col < cols and
            matrix[row][col] == string[plen] and not visited[row][col]):
        visited[row][col] = True
        plen += 1
        hasp = (has_path_core(matrix, row, col-1, rows, cols,
                              string, plen, visited) or
                has_path_core(matrix, row, col+1, rows, cols,
                              string, plen, visited) or
                has_path_core(matrix, row-1, col, rows, cols,
                              string, plen, visited) or
                has_path_core(matrix, row+1, col, rows, cols,
                              string, plen, visited)
                )
        if not hasp:
            plen -= 1
            visited[row][col] = False
    return hasp


if __name__ == '__main__':
    matrix = [
        ["A", "B", "T", "G"],
        ["C", "F", "C", "S"],
        ["J", "D", "E", "H"]]
    string = "BTGSHEDJCA"
    visited = [[False, False, False, False], [False, False, False, False], [False, False, False, False]]
    plen = 0
    res = has_path_core(matrix, 0, 1, 3, 4, string, plen, visited)
    print(res)
    res = has_path(matrix, string)
    print(res)



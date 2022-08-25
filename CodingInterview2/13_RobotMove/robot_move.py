"""
面试题 13：机器人的运动范围
题目：地上有一个 m 行 n 列的方格。一个机器人从坐标 (0, 0) 的格子开始移动，它
每一次可以向左、右、上、下移动一格，但不能进入行坐标和列坐标的数位之和
大于 k 的格子。例如，当 k 为 18 时，机器人能够进入方格 (35, 37)，因为 3+5+3+7=18。
但它不能进入方格 (35, 38)，因为 3+5+3+8=19。请问该机器人能够到达多少个格子？

"""


def moving_count(rows: int, cols: int, threshold: int) -> int:
    """
    Count moving steps under the given rows, clos and threshold.

    Parameters
    -----------
    rows: int
        Matrix rows
    cols: int
        Matrix cols
    threshold: int
        The given condition

    Returns
    ---------
    out: int
        How many cells can reach.

    Notes
    ------
    We could treat the (row, col) as the center of a cell.
    """
    if rows <= 0 or cols <= 0 or threshold < 0:
        return 0
    visited = []
    for i in range(rows):
        tmp = []
        for j in range(cols):
            tmp.append(False)
        visited.append(tmp)
    res = moving_count_core(rows, cols, 0, 0, threshold, visited)
    return res


def moving_count_core(rows, cols, row, col, threshold, visited) -> int:
    """
    Recursive caculation.

    Notes
    --------
    The key points are as belows:
    - condition threshold
    - condition visited
    - count 1+ because the cell it stands is surely it can enter.
    - do not need to go back
    """
    count = 0
    if (row >= 0 and row < rows and col >= 0 and col < cols and
        get_digit_num(row) + get_digit_num(col) <= threshold and
        not visited[row][col]):
        visited[row][col] = True
        count = 1 + (
            moving_count_core(rows, cols, row+1, col, threshold, visited) +
            moving_count_core(rows, cols, row-1, col, threshold, visited) +
            moving_count_core(rows, cols, row, col+1, threshold, visited) +
            moving_count_core(rows, cols, row, col-1, threshold, visited)
        )
    return count


def get_digit_num(num: int) -> int:
    """
    Return sum of each in a number.
    """
    res = 0
    while num:
        res += num % 10
        num //= 10
    return res


if __name__ == '__main__':
    res = moving_count(1, 2, 1)
    print(res)

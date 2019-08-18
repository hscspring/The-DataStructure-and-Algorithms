"""
面试题 4：二维数组中的查找
题目：在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按
照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个
整数，判断数组中是否含有该整数。

LeetCode: https://leetcode.com/problems/search-a-2d-matrix-ii/
"""



def find(matrix: list, x: int) -> bool:
    """
    Given a matrix and a number x, 
    judge whether x is in the matrix.
    The matrix is increased by rows from left to right and columns from up to down.
    
    Parameters
    ----------
    matrix: list
    x: int

    Returns
    --------
    out: bool

    """
    res = False
    row = 0
    m = len(matrix)
    col = len(matrix[0]) - 1
    while col > 0 and row < m:
        if matrix[row][col] > x:
            col -= 1
        elif matrix[row][col] < x:
            row += 1
        else:
            res = True
            break
    return res
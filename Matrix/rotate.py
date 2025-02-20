def rotate(matrix):
    n = len(matrix)

    # 第一步：转置矩阵
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # 第二步：反转每一行
    for i in range(n):
        for j in range(n // 2):
            matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1], matrix[i][j]

    return matrix


a = [
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]]
b = [
    [7, 4, 1], [8, 5, 2], [9, 6, 3]]


assert rotate(a) == b

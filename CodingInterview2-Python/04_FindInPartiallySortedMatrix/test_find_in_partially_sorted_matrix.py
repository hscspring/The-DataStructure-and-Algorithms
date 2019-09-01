from find_in_partially_sorted_matrix import find


def test_pass():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 100]]
    assert find(matrix, 3) == True
    assert find(matrix, 8) == True
    assert find(matrix, 0) == False
    assert find(matrix, 10) == False
    assert find(matrix, 101) == False

def test_irregularly_matrix():
    matrix = [[1, 2, 3], [4, 5, 9]]
    assert find(matrix, 2) == True
    assert find(matrix, 7) == False
    assert find(matrix, 10) == False

def test_blank_matrix():
    matrix = [[]]
    assert find(matrix, 0) == False
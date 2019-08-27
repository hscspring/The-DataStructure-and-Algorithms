from string_path_in_matrix import has_path

(A, B, C, D, E, F, G, H, I, J, K, L, M, N,
    O, P, Q, R, S, T, U, V, W, X, Y, Z) = (
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
    "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
)

def test_normal_in():
    matrix = [
        [A, B, T, G],
        [C, F, C, S],
        [J, D, E, H]]
    string = "BFCE"
    assert has_path(matrix, string) == True


def test_corner_in():
    matrix = [
        [A, B, C, E],
        [S, F, C, S],
        [A, D, E, E]]
    string = "SEE"
    assert has_path(matrix, string) == True


def test_normal_not_in():
    matrix = [
        [A, B, T, G],
        [C, F, C, S],
        [J, D, E, H]]
    string = "ABFB"
    assert has_path(matrix, string) == False


def test_long_string_in():
    matrix = [
        [A, B, C, E, H, J, I, G],
        [S, F, C, S, L, O, P, Q],
        [A, D, E, E, M, N, O, E],
        [A, D, I, D, E, J, F, M],
        [V, C, E, I, F, G, G, S]]
    string = "SLHECCEIDEJFGGFIE"
    assert has_path(matrix, string) == True


def test_long_string_border_in():
    matrix = [
        [A, B, C, E, H, J, I, G],
        [S, F, C, S, L, O, P, Q],
        [A, D, E, E, M, N, O, E],
        [A, D, I, D, E, J, F, M],
        [V, C, E, I, F, G, G, S]]
    string = "SGGFIECVAASABCEHJIGQEM"
    assert has_path(matrix, string) == True


def test_long_sting_not_in():
    matrix = [
        [A, B, C, E, H, J, I, G],
        [S, F, C, S, L, O, P, Q],
        [A, D, E, E, M, N, O, E],
        [A, D, I, D, E, J, F, M],
        [V, C, E, I, F, G, G, S]]
    string = "SGGFIECVAASABCEEJIGOEM"
    assert has_path(matrix, string) == False


def test_long_string_border_repeat_not_in():
    matrix = [
        [A, B, C, E, H, J, I, G],
        [S, F, C, S, L, O, P, Q],
        [A, D, E, E, M, N, O, E],
        [A, D, I, D, E, J, F, M],
        [V, C, E, I, F, G, G, S]]
    string = "SGGFIECVAASABCEHJIGQEMS"
    assert has_path(matrix, string) == False


def test_same_element_in():
    matrix = [
        [A, A, A, A],
        [A, A, A, A],
        [A, A, A, A]]
    string = "AAAAAAAAAAAA"
    assert has_path(matrix, string) == True


def test_same_element_not_in():
    matrix = [
        [A, A, A, A],
        [A, A, A, A],
        [A, A, A, A]]
    string = "AAAAAAAAAAAAA"
    assert has_path(matrix, string) == False


def test_single_in():
    matrix = [[A]]
    string = "A"
    assert has_path(matrix, string) == True


def test_single_not_in():
    matrix = [[A]]
    string = "B"
    assert has_path(matrix, string) == False


def test_matrix_none():
    matrix = [[]]
    string = "A"
    assert has_path(matrix, string) == False


def test_string_none():
    matrix = [[A]]
    string = ""
    assert has_path(matrix, string) == True


if __name__ == '__main__':
    print(A,B,C,D)

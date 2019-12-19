from sort_array_for_min_number import combine_to_min_num


def test_all_single():
    lst = [3, 5, 1, 4, 2]
    assert combine_to_min_num(lst) == "12345"


def test_normal1():
    lst = [3, 32, 321]
    assert combine_to_min_num(lst) == "321323"


def test_normal2():
    lst = [3, 323, 32123]
    assert combine_to_min_num(lst) == "321233233"


def tes_same():
    lst = [1, 11, 111]
    assert combine_to_min_num(lst) == "111111"


def test_single():
    lst = [321]
    assert combine_to_min_num(lst) == "321"


def test_contain_zero():
    lst = [9, 18, 0, 0]
    assert combine_to_min_num(lst) == "189"


def test_zeros():
    lst = [0, 0, 0]
    assert combine_to_min_num(lst) == ""


def test_none():
    lst = []
    assert combine_to_min_num(lst) == ""

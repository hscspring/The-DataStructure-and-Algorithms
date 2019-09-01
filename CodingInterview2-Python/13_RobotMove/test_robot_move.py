from robot_move import moving_count


def test_multi_rows_cols_small():
    assert moving_count(10, 10, 5) == 21

def test_multi_rows_cols_big():
    assert moving_count(20, 20, 15) == 359

def test_one_row_part():
    assert moving_count(1, 10, 3) == 4

def test_one_row_all():
    assert moving_count(1, 10, 9) == 10

def test_one_col_part():
    # 0-78
    assert moving_count(100, 1, 15) == 79

def test_one_col_all():
    assert moving_count(100, 1, 18) == 100

def test_one_row_one_col_zero_threshold():
    assert moving_count(1, 1, 0) == 1

def test_one_row_one_col():
    assert moving_count(1, 1, 2) == 1

def test_row_none():
    assert moving_count(0, 1, 0) == 0

def test_col_none():
    assert moving_count(1, 0, 0) == 0

def test_threshold_none():
    assert moving_count(1, 1, -1) == 0

def test_all_none():
    assert moving_count(-1, -1, -1) == 0
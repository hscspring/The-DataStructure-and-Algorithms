from greatest_sum_of_subarrays import find_greatest_sum_of_sub_array
from greatest_sum_of_subarrays import find_greatest_sum_of_sub_array_dp


def test_pos_neg():
    lst = [1, -2, 3, 10, -4, 7, 2, -5]
    assert find_greatest_sum_of_sub_array(lst) == 18
    assert find_greatest_sum_of_sub_array_dp(lst) == 18


def test_all_neg():
    lst = [-2, -8, -1, -5, -9]
    assert find_greatest_sum_of_sub_array(lst) == -1
    assert find_greatest_sum_of_sub_array_dp(lst) == -1


def test_all_pos():
    lst = [2, 8, 1, 5, 9]
    assert find_greatest_sum_of_sub_array(lst) == 25
    assert find_greatest_sum_of_sub_array_dp(lst) == 25


def test_none():
    assert find_greatest_sum_of_sub_array([]) == 0
    assert find_greatest_sum_of_sub_array_dp([]) == 0

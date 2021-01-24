from longest_substring_without_dup import find_sub_string_length_set
from longest_substring_without_dup import find_sub_string_length_dict
from longest_substring_without_dup import find_sub_string_length_dp1
from longest_substring_without_dup import find_sub_string_length_dp2

def test1():
    assert find_sub_string_length_set("abcacfrar") == 4
    assert find_sub_string_length_dict("abcacfrar") == 4
    assert find_sub_string_length_dp1("abcacfrar") == 4
    assert find_sub_string_length_dp2("abcacfrar") == 4


def test2():
    assert find_sub_string_length_set("acfrarabc") == 4
    assert find_sub_string_length_dict("acfrarabc") == 4
    assert find_sub_string_length_dp1("acfrarabc") == 4
    assert find_sub_string_length_dp2("acfrarabc") == 4


def test3():
    assert find_sub_string_length_set("arabcacfr") == 4
    assert find_sub_string_length_dict("arabcacfr") == 4
    assert find_sub_string_length_dp1("arabcacfr") == 4
    assert find_sub_string_length_dp2("arabcacfr") == 4


def test4():
    assert find_sub_string_length_set("aaaa") == 1
    assert find_sub_string_length_dict("aaaa") == 1
    assert find_sub_string_length_dp1("aaaa") == 1
    assert find_sub_string_length_dp2("aaaa") == 1


def test5():
    assert find_sub_string_length_set("abcdefg") == 7
    assert find_sub_string_length_dict("abcdefg") == 7
    assert find_sub_string_length_dp1("abcdefg") == 7
    assert find_sub_string_length_dp2("abcdefg") == 7


def test6():
    assert find_sub_string_length_set("aaabbbccc") == 2
    assert find_sub_string_length_dict("aaabbbccc") == 2
    assert find_sub_string_length_dp1("aaabbbccc") == 2
    assert find_sub_string_length_dp2("aaabbbccc") == 2


def test7():
    assert find_sub_string_length_set("abcdcba") == 4
    assert find_sub_string_length_dict("abcdcba") == 4
    assert find_sub_string_length_dp1("abcdcba") == 4
    assert find_sub_string_length_dp2("abcdcba") == 4


def test8():
    assert find_sub_string_length_set("abcdaef") == 6
    assert find_sub_string_length_dict("abcdaef") == 6
    assert find_sub_string_length_dp1("abcdaef") == 6
    assert find_sub_string_length_dp2("abcdaef") == 6


def test9():
    assert find_sub_string_length_set("a") == 1
    assert find_sub_string_length_dict("a") == 1
    assert find_sub_string_length_dp1("a") == 1
    assert find_sub_string_length_dp2("a") == 1


def test10():
    assert find_sub_string_length_set("") == 0
    assert find_sub_string_length_dict("") == 0
    assert find_sub_string_length_dp1("") == 0
    assert find_sub_string_length_dp2("") == 0

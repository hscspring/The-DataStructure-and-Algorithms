import pytest

from get_char_meta import split_comp_parts, get_comp
from get_char_meta import get_char_and_comp_rawdict


char_dict, comp_rawdict = get_char_and_comp_rawdict("dict/ids.txt")


def test_split_comp_parts1():
    s = "⿱亠田"
    assert split_comp_parts(s) == ["⿱", "亠田"]


def test_split_comp_parts2():
    s = "⿱⿳亠口冖儿[TJK]"
    assert split_comp_parts(s) == ["⿱", "⿳", "亠口冖儿[TJK]"]


def test_split_comp_parts3():
    s = "⿳⿳亠口冖⿻二丨九[T]"
    assert split_comp_parts(s) == ["⿳", "⿳", "亠口冖", "⿻", "二丨九[T]"]


def test_split_comp_parts4():
    s = "亠田"
    assert split_comp_parts(s) == ["亠田"]


def test_split_comp_parts5():
    s = "⿳"
    assert split_comp_parts(s) == ["⿳"]


def test_split_comp_parts6():
    s = "⿱⿳"
    assert split_comp_parts(s) == ["⿱", "⿳"]


def test_split_comp_parts7():
    s = ""
    assert split_comp_parts(s) == [""]


def test_get_comp1():
    s = "⿱亠田"
    lst = []
    get_comp(comp_rawdict, s, lst)
    res = "".join(lst)
    assert res == "⿱⿱丶一[GTK]田"


def test_get_comp2():
    s = "⿱⿳亠口冖儿[TJK]"
    lst = []
    get_comp(comp_rawdict, s, lst)
    res = "".join(lst)
    assert res == "⿱⿳⿱丶一[GTK]口冖⿰丿乚[TJK]"


def test_get_comp3():
    s = "⿳⿳亠口冖⿻二丨九[T]"
    lst = []
    get_comp(comp_rawdict, s, lst)
    res = "".join(lst)
    assert res == "⿳⿳⿱丶一[GTK]口冖⿻⿱一一丨九[T]"


def test_get_comp4():
    # 这里由于是纯字符串，直接返回
    s = "亠田"
    lst = []
    get_comp(comp_rawdict, s, lst)
    res = "".join(lst)
    # assert res == "⿱丶一[GTK]田"
    assert res == "亠田"


def test_get_comp5():
    # PAY ATTENTION to this test case.
    # 因为这种输入是不正常的，所以应该被当做普通字符串处理
    s = "⿱亠"
    lst = []
    get_comp(comp_rawdict, s, lst)
    res = "".join(lst)
    assert res == "⿱亠"


def test_get_comp6():
    # PAY ATTENTION to this test case.
    # 因为这种输入是不正常的，所以应该被当做普通字符串处理
    s = "⿱⿳亠"
    lst = []
    get_comp(comp_rawdict, s, lst)
    res = "".join(lst)
    assert res == "⿱⿳亠"


def test_get_comp7():
    s = "⿱⿳"
    lst = []
    get_comp(comp_rawdict, s, lst)
    res = "".join(lst)
    assert res == "⿱⿳"


def test_get_comp8():
    s = "⿱"
    lst = []
    get_comp(comp_rawdict, s, lst)
    res = "".join(lst)
    assert res == "⿱"


def test_get_comp9():
    s = ""
    lst = []
    get_comp(comp_rawdict, s, lst)
    res = "".join(lst)
    assert res == ""

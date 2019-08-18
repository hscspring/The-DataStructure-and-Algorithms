from replace_spaces import replace


def test_multi_spaces():
    s = "We are happy."
    assert replace(s) == "We%20are%20happy."
def test_front_space():
    s = " we"
    assert replace(s) == "%20we"

def test_back_space():
    s = "we "
    assert replace(s) == "we%20"

def test_no_space():
    s = "aaa"
    assert replace(s) == "aaa"

def test_none():
    s = ""
    assert replace(s) == ""

def test_one_space():
    s = " "
    assert replace(s) == "%20"

def test_multi_spaces():
    s = "  "
    assert replace(s) == "%20%20"
from first_not_repeating_char import first_not_repeat


def test_exist():
    assert first_not_repeat("google") == "l"


def test_not_exist():
    assert first_not_repeat("aabccdbd") == ""


def test_all_once():
    assert first_not_repeat("abcdefg") == "a"


def test_none():
    assert first_not_repeat("") == ""

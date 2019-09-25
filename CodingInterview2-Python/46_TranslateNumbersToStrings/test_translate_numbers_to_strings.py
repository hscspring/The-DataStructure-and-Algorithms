from translate_numbers_to_strings import get_translation_count


def test0():
    assert get_translation_count(0) == 1


def test10():
    assert get_translation_count(10) == 2


def test125():
    assert get_translation_count(125) == 3


def test126():
    assert get_translation_count(126) == 2


def test426():
    assert get_translation_count(426) == 1


def test100():
    assert get_translation_count(100) == 2


def test101():
    assert get_translation_count(101) == 2


def test12258():
    assert get_translation_count(12258) == 5


def testm100():
    assert get_translation_count(-100) == 0

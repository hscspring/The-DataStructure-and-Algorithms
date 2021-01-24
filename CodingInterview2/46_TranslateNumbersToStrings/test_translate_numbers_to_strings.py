from translate_numbers_to_strings import get_translation_count1
from translate_numbers_to_strings import get_translation_count2



def test0():
    assert get_translation_count1(0) == 1
    assert get_translation_count2(0) == 1


def test10():
    assert get_translation_count1(10) == 2
    assert get_translation_count2(10) == 2


def test25():
    assert get_translation_count1(25) == 2
    assert get_translation_count2(25) == 2

def test26():
    assert get_translation_count1(26) == 1
    assert get_translation_count2(26) == 1

def test125():
    assert get_translation_count1(125) == 3
    assert get_translation_count2(125) == 3


def test126():
    assert get_translation_count1(126) == 2
    assert get_translation_count2(126) == 2


def test426():
    assert get_translation_count1(426) == 1
    assert get_translation_count2(426) == 1


def test100():
    assert get_translation_count1(100) == 2
    assert get_translation_count2(100) == 2


def test101():
    assert get_translation_count1(101) == 2
    assert get_translation_count2(101) == 2


def test12258():
    assert get_translation_count1(12258) == 5
    assert get_translation_count2(12258) == 5


def testm100():
    assert get_translation_count1(-100) == 0
    assert get_translation_count2(-100) == 0

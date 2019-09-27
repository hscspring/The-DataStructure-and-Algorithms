from first_character_in_stream import first_appear_once


def test1():
    assert first_appear_once("g") == "g"


def test2():
    assert first_appear_once("o") == "g"


def test3():
    assert first_appear_once("o") == "g"


def test4():
    assert first_appear_once("g") == ""


def test5():
    assert first_appear_once("l") == "l"


def test6():
    assert first_appear_once("e") == "l"

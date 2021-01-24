from probability import get_probability
from probability import get_probability_recursion
from probability import get_probability_recursion2


def test1():
    assert get_probability(1) == 0
    assert get_probability_recursion(1) == 0
    assert get_probability_recursion2(1) == 0


def test2():
    assert get_probability(2) == 0
    assert get_probability_recursion(2) == 0
    assert get_probability_recursion2(2) == 0


def test3():
    assert get_probability(3) == 0
    assert get_probability_recursion(3) == 0
    assert get_probability_recursion2(3) == 0


def test4():
    assert get_probability(4) == 0
    assert get_probability_recursion(4) == 0
    assert get_probability_recursion2(4) == 0


def test11():
    assert get_probability(8) == 0
    assert get_probability_recursion(8) == 0
    assert get_probability_recursion2(8) == 0


def test0():
    assert get_probability(0) == 0
    assert get_probability_recursion(0) == 0
    assert get_probability_recursion2(0) == 0

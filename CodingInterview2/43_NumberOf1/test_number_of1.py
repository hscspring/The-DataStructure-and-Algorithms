from number_of1 import number_of_one
from number_of1 import number_of_one_recursion
from number_of1 import count_one

def test_single_1(n=1):
    assert number_of_one(n) == 1
    assert number_of_one_recursion(n) == 1
    assert count_one(n) == 1


def test_single_1(n=5):
    assert number_of_one(n) == 1
    assert number_of_one_recursion(n) == 1
    assert count_one(n) == 1


def test_two_2(n=10):
    assert number_of_one(n) == 2
    assert number_of_one_recursion(n) == 2
    assert count_one(n) == 2


def test_two_16(n=55):
    assert number_of_one(n) == 16
    assert number_of_one_recursion(n) == 16
    assert count_one(n) == 16


def test_two_20(n=99):
    assert number_of_one(n) == 20
    assert number_of_one_recursion(n) == 20
    assert count_one(n) == 20


def test_five_4001(n=10000):
    assert number_of_one(n) == 4001
    assert number_of_one_recursion(n) == 4001
    assert count_one(n) == 4001


def test_five_18821(n=21345):
    assert number_of_one(n) == 18821
    assert number_of_one_recursion(n) == 18821
    assert count_one(n) == 18821


def test_0(n=0):
    assert number_of_one(n) == 0
    assert number_of_one_recursion(n) == 0
    assert count_one(n) == 0

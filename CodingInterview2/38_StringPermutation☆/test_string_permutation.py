from string_permutation import permutate2


def test_none():
    s = ""
    assert permutate2(s) == []


def test_one():
    s = "a"
    assert permutate2(s) == ["a"]


def test_two():
    s = "ab"
    assert permutate2(s) == ["ab", "ba"]


def test_three():
    s = "abc"
    assert permutate2(s) == ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']


def test_four():
    s = "abcd"
    assert permutate2(s) == ['abcd', 'abdc', 'acbd', 'acdb', 'adbc', 'adcb',
                            'bacd', 'badc', 'bcad', 'bcda', 'bdac', 'bdca',
                            'cabd', 'cadb', 'cbad', 'cbda', 'cdab', 'cdba',
                            'dabc', 'dacb', 'dbac', 'dbca', 'dcab', 'dcba']

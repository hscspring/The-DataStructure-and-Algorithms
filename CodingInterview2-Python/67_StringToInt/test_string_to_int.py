from string_to_int import str2int


def test1():
    assert str2int("123") == 123


def test2():
    assert str2int("+123") == 123


def test22():
    assert str2int("++123") == 123


def test3():
    assert str2int("-123") == -123


def test33():
    assert str2int("--123") == 123


def test4():
    assert str2int("+0") == 0


def test40():
    assert str2int("++0") == 0


def test41():
    assert str2int("+02") == 0


def test42():
    assert str2int("++02") == 0


def test5():
    assert str2int("-0") == 0


def test50():
    assert str2int("--0") == 0


def test51():
    assert str2int("-02") == 0


def test52():
    assert str2int("--02") == 0


def test6():
    assert str2int("+") == 0


def test60():
    assert str2int("++") == 0


def test7():
    assert str2int("-") == 0


def test70():
    assert str2int("--") == 0


def test8():
    assert str2int("1a2") == 0


def test9():
    assert str2int("") == 0


def test10():
    # 最大整数，0x7FFFFFFF
    assert str2int("+2147483647") == 2147483647


def test11():
    assert str2int("-2147483647") == -2147483647


def test12():
    assert str2int("+2147483648") == 0


def test13():
    # 最小负数，0x80000000
    assert str2int("-2147483648") == -2147483648


def test14():
    assert str2int("+2147483649") == 0


def test15():
    assert str2int("-2147483649") == 0


def test16():
    assert str2int("0") == 0


def test17():
    assert str2int("000") == 0


def test18():
    assert str2int("001") == 0

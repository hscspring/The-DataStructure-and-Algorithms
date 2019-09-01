from numeric_strings import is_num



def test_pos():
    assert is_num("100") == True

def test_operator_pos():
    assert is_num("+100") == True

def test_neg():
    assert is_num("-123") == True

def test_deci():
    assert is_num("3.14") == True

def test_pos_dot():
    assert is_num("3.") == True

def test_neg_dot():
    assert is_num("-.123") == True

def test_pos_exp():
    assert is_num("5e2") == True

def test_deci_exp():
    assert is_num("123.56e2") == True

def test_deci_exp_operator():
    assert is_num("1.79234234235235E+308") == True

def test_neg_deci():
    assert is_num("-1E-16") == True

def test_all0():
    assert is_num("00000") == True

def test_pos_all0():
    assert is_num("+0000") == True

def test_neg_all0():
    assert is_num("-0000") == True

def test_pos_0head_deci():
    assert is_num("00001.1") == True

def test_neg_0head_deci():
    assert is_num("-00001.") == True

def test_0head_not():
    assert is_num("001") == False

def test_pos_0head_not():
    assert is_num("+001") == False

def test_neg_0head_not():
    assert is_num("-001") == False

def pos_operator_pos_not():
    assert is_num("1+2") == False

def test_exp_not():
    assert is_num("12e") == False

def test_contain_letter_not():
    assert is_num("1a3.14") == False

def test_multi_dot_not():
    assert is_num("1.2.3") == False

def test_multi_operator_not():
    assert is_num("+-5") == False

def test_deci_exp_not():
    assert is_num("12e+5.4") == False

def test_dot_not():
    assert is_num(".") == False

def test_dot_exp_pos_not():
    assert is_num(".e1") == False

def test_exp_pos_not():
    assert is_num("e1") == False

def test_operator_dot_not():
    assert is_num("+.") == False

def test_none():
    assert is_num("") == False







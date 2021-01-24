from regular_expressions import match_dp, match_recursion

def test_01():
    assert match_dp("", "") == True
    assert match_recursion("", "") == True

def test_02():
    assert match_dp("", ".*") == True
    assert match_recursion("", ".*") == True

def test_03():
    assert match_dp("", ".") == False
    assert match_recursion("", ".") == False

def test_04():
    assert match_dp("", "c*") == True
    assert match_recursion("", "c*") == True

def test_05():
    assert match_dp("a", "a.") == False
    assert match_recursion("a", "a.") == False

def test_06():
    assert match_dp("a", ".*..a*") == False
    assert match_recursion("a", ".*..a*") == False

def test_07():
    assert match_dp("a", ".*") == True
    assert match_recursion("a", ".*") == True

def test_08():
    assert match_dp("a", "") == False
    assert match_recursion("a", "") == False

def test_09():
    assert match_dp("a", ".") == True
    assert match_recursion("a", ".") == True

def test_10():
    assert match_dp("a", "ab*") == True
    assert match_recursion("a", "ab*") == True

def test_11():
    assert match_dp("a", "ab*a") == False
    assert match_recursion("a", "ab*a") == False

def test_12():
    assert match_dp("ab", ".*..c*") == True
    assert match_recursion("ab", ".*..c*") == True

def test_13():
    assert match_dp("ab", ".*..") == True
    assert match_recursion("ab", ".*..") == True

def test_14():
    assert match_dp("ab", ".*") == True
    assert match_recursion("ab", ".*") == True

def test_15():
    assert match_dp("ab", "a.") == True
    assert match_recursion("ab", "a.") == True

def test_16():
    assert match_dp("ab", "ab.*") == True
    assert match_recursion("ab", "ab.*") == True

def test_17():
    assert match_dp("ab", "a.*b") == True
    assert match_recursion("ab", "a.*b") == True

def test_18():
    assert match_dp("ab", "a.*b*") == True
    assert match_recursion("ab", "a.*b*") == True

def test_19():
    assert match_dp("aa", "a") == False
    assert match_recursion("aa", "a") == False

def test_20():
    assert match_dp("aa", "a*") == True
    assert match_recursion("aa", "a*") == True

def test_21():
    assert match_dp("aa", "a.") == True
    assert match_recursion("aa", "a.") == True

def test_22():
    assert match_dp("ac", "ab.*") == False
    assert match_recursion("ac", "ab.*") == False

def test_23():
    assert match_dp("ac", "a.*") == True
    assert match_recursion("ac", "a.*") == True

def test_24():
    assert match_dp("ax", "a.b*") == True
    assert match_recursion("ax", "a.b*") == True

def test_25():
    assert match_dp("aaa", ".*") == True
    assert match_recursion("aaa", ".*") == True

def test_26():
    assert match_dp("aaa", "a*a") == True
    assert match_recursion("aaa", "a*a") == True

def test_27():
    assert match_dp("aaa", "ab*ac*a") == True
    assert match_recursion("aaa", "ab*ac*a") == True

def test_28():
    assert match_dp("aaa", "ab*a*c*a") == True
    assert match_recursion("aaa", "ab*a*c*a") == True

def test_29():
    assert match_dp("aab", "c*a*b") == True
    assert match_recursion("aab", "c*a*b") == True

def test_30():
    assert match_dp("abb", "a.*b*") == True
    assert match_recursion("abb", "a.*b*") == True

def test_31():
    assert match_dp("abc", "a.*") == True
    assert match_recursion("abc", "a.*") == True

def test_32():
    assert match_dp("axb", "a.b*") == True
    assert match_recursion("axb", "a.b*") == True

def test_33():
    assert match_dp("axc", "a.b*") == False
    assert match_recursion("axc", "a.b*") == False

def test_34():
    assert match_dp("abcde", "ab.*") == True
    assert match_recursion("abcde", "ab.*") == True

def test_35():
    assert match_dp("mississippi", "mis*is*p*.") == False
    assert match_recursion("mississippi", "mis*is*p*.") == False




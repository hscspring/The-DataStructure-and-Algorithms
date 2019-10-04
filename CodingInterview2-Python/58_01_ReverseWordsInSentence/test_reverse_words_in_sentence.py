from reverse_words_in_sentence import reverse_sentence, reverse_sentence_easy
from reverse_words_in_sentence import reverse_sentence_no_builtin

# 功能测试，句子中有多个单词
def test1():
    s = "I am a student."
    assert reverse_sentence(s) == "student. a am I"
    assert reverse_sentence_easy(s) == "student. a am I"
    assert reverse_sentence_no_builtin(s) == "student. a am I"


# 功能测试，句子中只有一个单词
def test2():
    s = "Wonderful"
    assert reverse_sentence(s) == "Wonderful"
    assert reverse_sentence_easy(s) == "Wonderful"
    assert reverse_sentence_no_builtin(s) == "Wonderful"


# 边界值测试，测试空字符串
def test4():
    s = ""
    assert reverse_sentence(s) == ""
    assert reverse_sentence_easy(s) == ""
    assert reverse_sentence_no_builtin(s) == ""


# 边界值测试，字符串中只有空格
def test5():
    s = "   "
    assert reverse_sentence(s) == "   "
    assert reverse_sentence_easy(s) == "   "
    assert reverse_sentence_no_builtin(s) == "   "

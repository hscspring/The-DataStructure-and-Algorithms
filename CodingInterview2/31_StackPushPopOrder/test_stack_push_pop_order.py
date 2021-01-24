from stack_push_pop_order import is_pop_order, is_pop_order2


def test_normal_is1():
    push = [1, 2, 3, 4, 5]
    pop = [4, 5, 3, 2, 1]
    assert is_pop_order(push, pop) == True
    push = [1, 2, 3, 4, 5]
    pop = [4, 5, 3, 2, 1]
    assert is_pop_order2(push, pop) == True


def test_normal_is2():
    push = [1, 2, 3, 4, 5]
    pop = [3, 5, 4, 2, 1]
    assert is_pop_order(push, pop) == True
    push = [1, 2, 3, 4, 5]
    pop = [3, 5, 4, 2, 1]
    assert is_pop_order2(push, pop) == True


def test_normal_is3():
    push = [1, 2, 3, 4, 5]
    pop = [4, 3, 2, 1, 5]
    assert is_pop_order(push, pop) == True
    push = [1, 2, 3, 4, 5]
    pop = [4, 3, 2, 1, 5]
    assert is_pop_order2(push, pop) == True


def test_normal_is4():
    push = [1, 2, 3, 4, 5]
    pop = [4, 3, 5, 2, 1]
    assert is_pop_order(push, pop) == True
    push = [1, 2, 3, 4, 5]
    pop = [4, 3, 5, 2, 1]
    assert is_pop_order2(push, pop) == True



def test_normal_is5():
    push = [1, 2, 3, 4, 5]
    pop = [4, 3, 2, 5, 1]
    assert is_pop_order(push, pop) == True
    push = [1, 2, 3, 4, 5]
    pop = [4, 3, 2, 5, 1]
    assert is_pop_order2(push, pop) == True


def test_normal_isnot1():
    push = [1, 2, 3, 4, 5]
    pop = [4, 3, 5, 1, 2]
    assert is_pop_order(push, pop) == False
    push = [1, 2, 3, 4, 5]
    pop = [4, 3, 5, 1, 2]
    assert is_pop_order2(push, pop) == False


def test_normal_isnot2():
    push = [1, 2, 3, 4, 5]
    pop = [3, 5, 4, 1, 2]
    assert is_pop_order(push, pop) == False
    push = [1, 2, 3, 4, 5]
    pop = [3, 5, 4, 1, 2]
    assert is_pop_order2(push, pop) == False


def test_one_num_is():
    push = [1]
    pop = [1]
    assert is_pop_order(push, pop) == True
    push = [1]
    pop = [1]
    assert is_pop_order2(push, pop) == True


def test_one_num_isnot():
    push = [2]
    pop = [1]
    assert is_pop_order(push, pop) == False
    push = [2]
    pop = [1]
    assert is_pop_order2(push, pop) == False


def test_both_none():
    push = []
    pop = []
    assert is_pop_order(push, pop) == False
    assert is_pop_order2(push, pop) == False


def test_push_none():
    push = []
    pop = [1]
    assert is_pop_order(push, pop) == False
    push = []
    pop = [1]
    assert is_pop_order2(push, pop) == False


def test_pop_none():
    push = [1]
    pop = []
    assert is_pop_order(push, pop) == False
    push = [1]
    pop = []
    assert is_pop_order2(push, pop) == False

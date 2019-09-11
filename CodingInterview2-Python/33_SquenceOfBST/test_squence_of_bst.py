from squence_of_bst import verify_seq_bst, verify_seq_bst2


def test_full():
    #            10
    #         /      \
    #        6        14
    #       /\        /\
    #      4  8     12  16
    lst = [4, 8, 6, 12, 16, 14, 10]
    assert verify_seq_bst(lst) == True
    assert verify_seq_bst2(lst) == True


def test_not_full():
    #           5
    #          / \
    #         4   7
    #            /
    #           6
    lst = [4, 6, 7, 5]
    assert verify_seq_bst(lst) == True
    assert verify_seq_bst2(lst) == True


def test_left():
    #               5
    #              /
    #             4
    #            /
    #           3
    #          /
    #         2
    #        /
    #       1
    lst = [1, 2, 3, 4, 5]
    assert verify_seq_bst(lst) == True
    assert verify_seq_bst2(lst) == True


def test_right():
    # 1
    #  \
    #   2
    #    \
    #     3
    #      \
    #       4
    #        \
    #         5
    lst = [5, 4, 3, 2, 1]
    assert verify_seq_bst(lst) == True
    assert verify_seq_bst2(lst) == True


def test_single():
    lst = [5]
    assert verify_seq_bst(lst) == True
    assert verify_seq_bst2(lst) == True


def test_not1():
    lst = [7, 4, 6, 5]
    assert verify_seq_bst(lst) == False
    assert verify_seq_bst2(lst) == False


def test_not2():
    lst = [4, 6, 12, 8, 16, 14, 10]
    assert verify_seq_bst(lst) == False
    assert verify_seq_bst2(lst) == False


def test_none():
    lst = []
    assert verify_seq_bst(lst) == False
    assert verify_seq_bst2(lst) == False

from first_common_nodes_in_lists import lst2link, find_first_common_node


def test_in_middle():
    link1 = lst2link([1, 2, 3, 6, 7])
    link2 = lst2link([4, 5, 6, 7])
    res = find_first_common_node(link1, link2)
    assert res.val == 6


def test_no():
    link1 = lst2link([1, 2, 3, 4])
    link2 = lst2link([5, 6, 7])
    res = find_first_common_node(link1, link2)
    assert res == None


def test_in_last():
    link1 = lst2link([1, 2, 3, 4, 7])
    link2 = lst2link([5, 6, 7])
    res = find_first_common_node(link1, link2)
    assert res.val == 7


def test_same():
    link1 = lst2link([1, 2, 3, 4, 5])
    link2 = lst2link([1, 2, 3, 4, 5])
    res = find_first_common_node(link1, link2)
    assert res.val == 1


def test_one_no():
    link1 = lst2link([1, 2, 3, 4, 5])
    link2 = lst2link([])
    res = find_first_common_node(link1, link2)
    assert res == None


def test_none():
    link1 = lst2link([])
    link2 = lst2link([])
    res = find_first_common_node(link1, link2)
    assert res == None

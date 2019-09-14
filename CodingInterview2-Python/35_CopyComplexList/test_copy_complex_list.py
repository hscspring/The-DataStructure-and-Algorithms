from copy_complex_list import clone_list_nodes, clone_list_nodes_with_dict
from copy_complex_list import ComplexNode, connect_nodes, print_list


def test_normal():
    a = ComplexNode(1)
    b = ComplexNode(2)
    c = ComplexNode(3)
    d = ComplexNode(4)
    e = ComplexNode(5)
    connect_nodes(a, b, c)
    connect_nodes(b, c, e)
    connect_nodes(c, d, None)
    connect_nodes(d, e, b)
    lst = print_list(a)
    res = clone_list_nodes(a)
    assert print_list(res) == lst
    res = clone_list_nodes_with_dict(a)
    assert print_list(res) == lst


def test_point_self():
    a = ComplexNode(1)
    b = ComplexNode(2)
    c = ComplexNode(3)
    d = ComplexNode(4)
    e = ComplexNode(5)
    connect_nodes(a, b, None)
    connect_nodes(b, c, e)
    connect_nodes(c, d, c)
    connect_nodes(d, e, b)
    lst = print_list(a)
    res = clone_list_nodes(a)
    assert print_list(res) == lst
    res = clone_list_nodes_with_dict(a)
    assert print_list(res) == lst


def test_point_loop():
    a = ComplexNode(1)
    b = ComplexNode(2)
    c = ComplexNode(3)
    d = ComplexNode(4)
    e = ComplexNode(5)
    connect_nodes(a, b, None)
    connect_nodes(b, c, d)
    connect_nodes(c, d, None)
    connect_nodes(d, e, b)
    lst = print_list(a)
    res = clone_list_nodes(a)
    assert print_list(res) == lst
    res = clone_list_nodes_with_dict(a)
    assert print_list(res) == lst


def test_one():
    a = ComplexNode(1)
    connect_nodes(a, None, a)
    lst = print_list(a)
    res = clone_list_nodes(a)
    assert print_list(res) == lst
    res = clone_list_nodes_with_dict(a)
    assert print_list(res) == lst


def test_none():
    a = None
    lst = print_list(a)
    res = clone_list_nodes(a)
    assert print_list(res) == lst
    res = clone_list_nodes_with_dict(a)
    assert print_list(res) == lst

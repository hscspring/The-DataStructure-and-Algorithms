from print_list_in_reversed_order import print_list_reverse
from print_list_in_reversed_order import print_list_reverse_recursive
from print_list_in_reversed_order import lst2link

def test_multi_nodes():
    node = lst2link([1, 2, 3])
    res = []
    print_list_reverse_recursive(node, res)
    assert res == [3, 2, 1]
    assert print_list_reverse(node) == [3, 2, 1]
    

def test_one_node():
    node = lst2link([1])
    res = []
    print_list_reverse_recursive(node, res)
    assert res == [1]
    assert print_list_reverse(node) == [1]

def test_none_node():
    node = lst2link([])
    res = []
    print_list_reverse_recursive(node, res)
    assert res == []
    assert print_list_reverse(node) == []

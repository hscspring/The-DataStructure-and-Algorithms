from entry_node_in_list_loop import find_entry_node_of_loop, find_entry_node_of_loop2
from entry_node_in_list_loop import list2link, list2link_withloop

def test_one_node_without_loop():
    lst = [1]
    link = list2link(lst)
    assert find_entry_node_of_loop(link) == None
    assert find_entry_node_of_loop2(link) == None

def test_one_node_with_loop():
    lst = [1]
    link = list2link_withloop(lst, 0)
    assert find_entry_node_of_loop(link).val == 1
    assert find_entry_node_of_loop2(link).val == 1

def test_multi_nodes_without_loop():
    lst = [1,2,3,4,5]
    link = list2link(lst)
    assert find_entry_node_of_loop(link) == None
    assert find_entry_node_of_loop2(link) == None

def test_multi_nodes_with_loop_head():
    lst = [1,2,3,4,5]
    link = list2link_withloop(lst, 0)
    assert find_entry_node_of_loop(link).val == 1
    assert find_entry_node_of_loop2(link).val == 1

def test_multi_nodes_with_loop_tail():
    lst = [1,2,3,4,5]
    link = list2link_withloop(lst, 4)
    assert find_entry_node_of_loop(link).val == 5
    assert find_entry_node_of_loop2(link).val == 5

def test_multi_nodes_with_loop_middle():
    lst = [1,2,3,4,5]
    link = list2link_withloop(lst, 2)
    assert find_entry_node_of_loop(link).val == 3
    assert find_entry_node_of_loop2(link).val == 3

def test_none():
    lst = []
    link = list2link(lst)
    assert find_entry_node_of_loop(link) == None
    assert find_entry_node_of_loop2(link) == None
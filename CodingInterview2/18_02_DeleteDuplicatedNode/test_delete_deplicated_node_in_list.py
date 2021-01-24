from delete_duplicated_node_in_list import delete_duplicated_node, list2link, link2list




def test_normal():
    root = list2link([1,2,2,4,5])
    root_new = delete_duplicated_node(root)
    assert link2list(root_new) == [1,4,5]

def test_head():
    root = list2link([1,1,3,4,5])
    root_new = delete_duplicated_node(root)
    assert link2list(root_new) == [3,4,5]

def test_tail():
    root = list2link([1,2,3,5,5])
    root_new = delete_duplicated_node(root)
    assert link2list(root_new) == [1,2,3]

def test_head_tail():
    root = list2link([1,1,3,5,5])
    root_new = delete_duplicated_node(root)
    assert link2list(root_new) == [3]

def test_all_duplicated():
    root = list2link([1,1])
    root_new = delete_duplicated_node(root)
    assert link2list(root_new) == []

def test_all_not_duplicated():
    root = list2link([1,2,3,4,5])
    root_new = delete_duplicated_node(root)
    assert link2list(root_new) == [1,2,3,4,5]

def test_pairs():
    root = list2link([1,1,2,2,3,3,4,4])
    root_new = delete_duplicated_node(root)
    assert link2list(root_new) == []

def test_two_not_duplicated():
    root = list2link([1,2])
    root_new = delete_duplicated_node(root)
    assert link2list(root_new) == [1,2]

def test_one_many_duplicated():
    root = list2link([1,1,1,1,2])
    root_new = delete_duplicated_node(root)
    assert link2list(root_new) == [2]

def test_single():
    root = list2link([1])
    root_new = delete_duplicated_node(root)
    assert link2list(root_new) == [1]

def test_none():
    root = list2link([])
    root_new = delete_duplicated_node(root)
    assert link2list(root_new) == []


    

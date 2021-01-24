from delete_node_in_list import delete_node, list2link, link2list




def test_normal():
    root = list2link([1,2,3,4,5])
    root_new = delete_node(root, root.next.next)
    assert link2list(root_new) == [1,2,4,5]

def test_head():
    root = list2link([1,2,3,4,5])
    root_new = delete_node(root, root)
    assert link2list(root_new) == [2,3,4,5]

def test_tail():
    root = list2link([1,2,3,4,5])
    root_new = delete_node(root, root.next.next.next.next)
    assert link2list(root_new) == [1,2,3,4]

def test_one():
    root = list2link([1])
    root_new = delete_node(root, root)
    assert link2list(root_new) == []

def test_none():
    root = list2link([])
    root_new = delete_node(root, root)
    assert link2list(root_new) == []

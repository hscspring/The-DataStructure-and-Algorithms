"""
面试题 36：二叉搜索树与双向链表
题目：输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求
不能创建任何新的结点，只能调整树中结点指针的指向。


"""


class BSTNode:
    """docstring for BSTNode"""
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# class LinkedList:
#     def __init__(self, val):
#         self.val = val
#         self.next = None
#         self.prev = None


def connect_bst_nodes(head: BSTNode, left: BSTNode, right: BSTNode) -> BSTNode:
    if head:
        head.left = left
        head.right = right


def travel_inorder(head: BSTNode, res: list) -> list:
    if head.left:
        res = travel_inorder(head.left, res)
    res.append(head.val)
    if head.right:
        res = travel_inorder(head.right, res)
    return res


def travel_linked_list(head: BSTNode) -> list:
    res = []
    while head:
        if head.left:
            res.append(head.left.val)
        else:
            res.append(None)

        res.append(head.val)

        if head.right:
            res.append(head.right.val)
        else:
            res.append(None)
        head = head.right
    return res


def convert_bst_to_sorted_doubly_linked_list_with_inorder(bst: BSTNode) -> BSTNode:
    if not bst:
        return None
    # it's important to add [] to the travel_inorder
    inorder = travel_inorder(bst, [])
    head = BSTNode(inorder[0])
    node = head
    for i in inorder[1:]:
        tmp = BSTNode(i)
        node.right = tmp
        tmp.left = node
        node = tmp
    return head




def convert_bst_to_sorted_doubly_linked_list(bst: BSTNode) -> BSTNode:
    """
    convert a bst to a sorted doubly linked list.

    Parameters
    -----------
    bst: the given bst.

    Returns
    ---------
    out: a doubly linked list.

    Notes
    ------

    """
    head = convert(bst, None)
    while head and head.left:
        head = head.left
    return head

def convert(bst: BSTNode, last: BSTNode):
    if not bst:
        return None
    curr = bst
    if curr.left:
        last = convert(curr.left, last)
    
    curr.left = last
    if last:
        last.right = curr
    last = curr
    
    if curr.right:
        last = convert(curr.right, last)
    return last

if __name__ == '__main__':
    #      10
    #   6      14
    # 4   8   12  16
    # tree = BSTNode(10)
    # connect_bst_nodes(tree, BSTNode(6), BSTNode(14))
    # connect_bst_nodes(tree.left, BSTNode(4), BSTNode(8))
    # connect_bst_nodes(tree.right, BSTNode(12), BSTNode(16))
    # res = travel_inorder(tree)
    # print(res)

    # tree = BSTNode(10)
    # connect_bst_nodes(tree, BSTNode(6), BSTNode(14))
    # connect_bst_nodes(tree.left, BSTNode(4), BSTNode(8))
    # connect_bst_nodes(tree.right, BSTNode(12), BSTNode(16))
    # head = convert_bst_to_sorted_doubly_linked_list(tree)
    # res = travel_linked_list(head)
    # print(res)


    tree = BSTNode(5)
    head = convert_bst_to_sorted_doubly_linked_list(tree)
    # head = convert_bst_to_sorted_doubly_linked_list_with_inorder(tree)
    res = travel_linked_list(head)
    print(res)
    # assert travel_linked_list(head) == [None, 4, 6, 4, 6, 8, 6, 8, 10, 8, 10, 12, 10, 12, 14, 12, 14, 16, 14, 16, None]
    # head = convert_bst_to_sorted_doubly_linked_list_with_inorder(tree)
    # assert travel_linked_list(head) == [None, 4, 6, 4, 6, 8, 6, 8, 10, 8, 10, 12, 10, 12, 14, 12, 14, 16, 14, 16, None]





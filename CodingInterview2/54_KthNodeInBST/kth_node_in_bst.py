"""
面试题 54：二叉搜索树的第 k 个结点
题目：给定一棵二叉搜索树，请找出其中的第 k 大的结点。

"""

class BSTNode:
    """docstring for BSTNode"""
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def connect_bst_nodes(head: BSTNode, left: BSTNode, right: BSTNode) -> BSTNode:
    if head:
        head.left = left
        head.right = right

def kth_node(bst: BSTNode, k: int) -> int:
    """
    

    Parameters
    -----------
    lst: the given bst
    k: kth

    Returns
    ---------
    the Kth BST Node value

    Notes
    ------
    inorder travel
    """
    if not bst or not k:
        return -1
    inorder = []
    travel_inorder(bst, inorder)
    if len(inorder) < k:
        return -1
    return inorder[k-1]

def travel_inorder(bst: BSTNode, res):
    if bst:
        travel_inorder(bst.right, res)
        res.append(bst.val)
        travel_inorder(bst.left, res)


def kth_node2(bst: BSTNode, k: int) -> int:
    # 参考 https://www.geeksforgeeks.org/find-n-th-node-inorder-traversal/
    if not bst or not k:
        return -1
    res = []
    count = [0]
    def travel_inorder2(bst: BSTNode, k: int):
        if bst and count[0] < k:
            travel_inorder2(bst.right, k)
            count[0] += 1
            if count[0] == k: 
                res.append(bst.val)
            travel_inorder2(bst.left, k)
    travel_inorder2(bst, k)
    return -1 if not res else res[0]


if __name__ == '__main__':
    tree = BSTNode(10)
    connect_bst_nodes(tree, BSTNode(6), BSTNode(14))
    connect_bst_nodes(tree.left, BSTNode(4), BSTNode(8))
    connect_bst_nodes(tree.right, BSTNode(12), BSTNode(16))
    # res = kth_node(tree, 3)
    # print(res)

    # res = []
    # travel_inorder(tree, res)
    # print(res)

    # res = kth_node(tree, 3)
    # print(res)


    # travel_inorder2(tree, 3, 0)
    # res = []
    # travel_inorder2(tree, 3, res)
    # print(res)


    res = kth_node2(tree, 1)
    print(res)

    res = kth_node2(tree, 2)
    print(res)






    
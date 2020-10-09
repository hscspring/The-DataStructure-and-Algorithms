class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def connect_nodes(head: TreeNode, left: TreeNode, right: TreeNode) -> TreeNode:
    if head:
        head.left = left
        head.right = right


def traversal_preorder(root: TreeNode):
    res = []

    def travel(root, res):
        if root:
            res.append(root.val)
            if root.left:
                travel(root.left, res)
            if root.right:
                travel(root.right, res)
    travel(root, res)
    return res


def traversal_inorder(root: TreeNode):
    res = []

    def travel(root, res):
        if root:
            if root.left:
                travel(root.left, res)
            res.append(root.val)
            if root.right:
                travel(root.right, res)
    travel(root, res)
    return res


def traversal_postorder(root: TreeNode):
    res = []

    def travel(root, res):
        if root:
            if root.left:
                travel(root.left, res)
            if root.right:
                travel(root.right, res)
            res.append(root.val)
    travel(root, res)
    return res


def traversal_preorder_iteration(root: TreeNode):
    """https://leetcode.com/problems/binary-tree-preorder-traversal/discuss/838862/Two-different-iteration-solutions-in-C%2B%2B-and-Python3"""
    res = []
    if not root:
        return []
    stack = [root]
    while stack:
        node = stack.pop()
        res.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return res


def traversal_inorder_iteration(root: TreeNode):
    res = []
    stack = []
    curr = root
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        res.append(curr.val)
        curr = curr.right
    return res


def traversal_postorder_iteration(root: TreeNode):
    """From https://leetcode.com/problems/binary-tree-postorder-traversal/discuss/830858/Python-recursive-generator-and-iterative-using-deque."""
    res = []
    stack = []
    curr = root
    while stack or curr:
        if curr:
            stack.append(curr)
            res.insert(0, curr.val)
            curr = curr.right
            continue
        curr = stack.pop()
        curr = curr.left
    return res


def traversal_preorder_morris(root: TreeNode):
    pass



def traversal_inorder_morris(root: TreeNode):
    res = []
    curr = root
    prev = None
    while curr:
        if not curr.left:
            res.append(curr.val)
            curr = curr.right
        else:
            prev = curr.left
            while prev.right:
                prev = prev.right
            tmp = curr
            prev.right = curr
            curr = curr.left
            tmp.left = None
    return res



def traversal_postorder_morris(root: TreeNode):
    pass



def traversal_hierarchically(root: TreeNode):
    if not root:
        return []
    res = []
    stack = [root]
    while stack:
        node = stack.pop(0)
        res.append(node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return res


def print_node(node: TreeNode):
    if node:
        print("node value: ", node.val)
        if node.left:
            print("left child value: ", node.left.val)
        else:
            print("left child null")
        if node.right:
            print("right child value: ", node.right.val)
        else:
            print("right child null")
    else:
        print("node is null")


def print_tree(root: TreeNode):
    print_node(root)
    if root:
        if root.left:
            print_tree(root.left)
        if root.right:
            print_tree(root.right)


if __name__ == '__main__':
    import copy
    tree = TreeNode('F')
    connect_nodes(tree, TreeNode('B'), TreeNode('G'))
    connect_nodes(tree.left, TreeNode('A'), TreeNode('D'))
    connect_nodes(tree.right, None, TreeNode('I'))
    connect_nodes(tree.left.right, TreeNode('C'), TreeNode('E'))
    connect_nodes(tree.right.right, TreeNode('H'), None)

    # print_tree(tree)

    print("Pre Order:")
    root = copy.deepcopy(tree)
    preorder = traversal_preorder(root)
    print(preorder)
    iterative_preorder = traversal_preorder_iteration(root)
    print(iterative_preorder)

    print("In Order: ")
    root = copy.deepcopy(tree)
    inorder = traversal_inorder(root)
    print(inorder)
    iterative_inorder = traversal_inorder_iteration(root)
    print(iterative_inorder)
    morris_inorder = traversal_inorder_morris(root)
    print(morris_inorder)

    print("Post Order: ")
    root = copy.deepcopy(tree)
    postorder = traversal_postorder(root)
    print(postorder)
    iterative_postorder = traversal_postorder_iteration(root)
    print(iterative_postorder)

    print("Hierarchical Order: ")
    root = copy.deepcopy(tree)
    hierarchicalorder = traversal_hierarchically(root)
    print(hierarchicalorder)

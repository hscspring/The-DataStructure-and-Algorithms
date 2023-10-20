from tree import TreeNode, connect_nodes, print_binary_tree3


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


############# Iteration ###############


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

def traversal_preorder_iteration2(root: TreeNode):
    res = []
    stack = []
    curr = root
    while stack or curr:
        while curr:
            res.append(curr.val)
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        curr = curr.right
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
    res =[]
    stack = []
    curr = root
    prev = None
    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack[-1]
        if curr.right and curr.right != prev:
            curr = curr.right
        else:
            stack.pop()
            res.append(curr.val)
            prev = curr
            curr = None
    return res

def traversal_postorder_iteration2(root: TreeNode):
    """From https://leetcode.com/problems/binary-tree-postorder-traversal/discuss/830858/Python-recursive-generator-and-iterative-using-deque."""
    res = []
    stack = []
    curr = root
    while stack or curr:
        while curr:
            res.append(curr.val)
            stack.append(curr)
            curr = curr.right
        curr = stack.pop()
        curr = curr.left
    return list(reversed(res))

############### BFS/DFS/HFS ############


def traversal_hierarchically(root: TreeNode):
    res = []
    queue = [root]
    while queue:
        tmp = []
        for i in range(len(queue)):
            node = queue.pop(0)
            tmp.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        res.append(tmp)
    return res


def traversal_dfs(root: TreeNode):
    res = []
    stack = [root]
    while stack:
        curr = stack.pop()
        res.append(curr.val)
        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)
    return res

def traversal_dfs_r(root):
    res = []
    def func(curr):
        res.append(curr.val)
        if curr.left:
            func(curr.left)
        if curr.right:
            func(curr.right)
    func(root)
    return res

def traversal_bfs(root: TreeNode):
    res = []
    queue = [root]
    while queue:
        curr = queue.pop(0)
        res.append(curr.val)
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)
    return res


############ Morris ###############


def traversal_preorder_morris(root: TreeNode):
    res = []
    curr = root
    prev = None
    while curr:
        if not curr.left:
            res.append(curr.val)
            curr = curr.right
        else:
            prev = curr.left
            while prev.right and prev.right is not curr:
                prev = prev.right
            if prev.right is curr:
                prev.right = None
                curr = curr.right
            else:
                res.append(curr.val)
                prev.right = curr
                curr = curr.left
    return res


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
            while prev.right and prev.right is not curr:
                prev = prev.right
            if prev.right is None:
                prev.right = curr
                curr = curr.left
            else:
                res.append(curr.val)
                prev.right = None
                curr = curr.right
    return res


def traversal_postorder_morris(root: TreeNode):
    res = []
    tmp = root
    visited = set()
    while tmp and tmp not in visited:
        if tmp.left and tmp.left not in visited:
            tmp = tmp.left
        elif tmp.right and tmp.right not in visited:
            tmp = tmp.right
        else:
            res.append(tmp.val)
            visited.add(tmp)
            tmp = root
    return res



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
    morris_preorder = traversal_preorder_morris(root)
    print(morris_preorder)

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
    morris_postorder = traversal_postorder_morris(root)
    print(morris_postorder)

    print("Hierarchical Order: ")
    root = copy.deepcopy(tree)
    hierarchicalorder = traversal_hierarchically(root)
    print(hierarchicalorder)

    print(print_binary_tree3(root))

    tree = TreeNode(6)
    connect_nodes(tree, TreeNode(4), TreeNode(9))
    connect_nodes(tree.left, None, TreeNode(18))
    connect_nodes(tree.right, None, TreeNode(26))
    connect_nodes(tree.left.right, None, TreeNode(32))
    connect_nodes(tree.right.right, TreeNode(12), None)
    connect_nodes(tree.right.right.left, TreeNode(10), TreeNode(30))
    connect_nodes(tree.right.right.left.right, TreeNode(8), TreeNode(45))
    root = copy.deepcopy(tree)
    preorder = traversal_preorder(root)
    print(preorder)

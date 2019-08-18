"""
面试题 8：二叉树的下一个结点
题目：给定一棵二叉树和其中的一个结点，如何找出中序遍历顺序的下一个结点？
树中的结点除了有两个分别指向左右子结点的指针以外，还有一个指向父结点的指针。

"""



class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

def get_next_in_inorder(pnode: TreeNode) -> TreeNode:
    if not pnode:
        return None
    pnext = None
    if pnode.right:
        pright = pnode.right
        while pright.left:
            pright = pright.left
        pnext = pright
    # DO NOT have a right tree
    # 没有右子树时
    elif pnode.parent:
        curr = pnode
        parent = pnode.parent
        # is his parent's right tree
        # 没有右子树，还是父节点的右子树
        # 沿着指向父节点的指针一直向上遍历，直到找到一个是它父节点的左子节点的节点
        while parent and curr == parent.right:
            curr = parent
            parent = parent.parent
        pnext = parent
    return pnext

def travel_inorder(tree: TreeNode):
    if tree:
        travel_inorder(tree.left)
        print(tree.val)
        travel_inorder(tree.right)

def connect_nodes(parent: TreeNode, left: TreeNode, right: TreeNode) -> TreeNode:
    if parent:
        parent.left = left
        parent.right = right
    if left:
        left.parent = parent
    if right:
        right.parent = parent
    return parent

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
    tree = TreeNode(5)
    connect_nodes(tree, TreeNode(4), None)
    connect_nodes(tree.left, TreeNode(3), None)
    connect_nodes(tree.left.left, TreeNode(2), TreeNode(1))
    pnext = get_next_in_inorder(tree.left.left.right)
    print_node(pnext)
    # travel_inorder(tree)




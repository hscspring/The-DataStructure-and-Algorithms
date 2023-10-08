
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def connect_nodes(head: TreeNode, left: TreeNode, right: TreeNode) -> TreeNode:
    if head:
        head.left = left
        head.right = right


def print_binary_tree3(tree: TreeNode) -> list:
    if not tree:
        return []
    queue, res = [tree], []
    while queue:
        tmp = []
        for i in range(len(queue)):
            node = queue.pop(0)
            tmp.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        if tmp:
            res.append(tmp)
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

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 二叉搜索树
def find_path_bst(root, target):
    path = []
    node = root
    while node and node.val != target:
        path.append(node.val)
        if taget < node.val:
            node = node.left
        else:
            node = node.right
    path.append(node.val)
    return path


# 二叉树给定节点路径
def find_path(root, target):
    if root is None:
        return []
    stack = [(root, [root.val])]
    while stack:
        node, path = stack.pop()
        if node.val == target:
            return path
        if node.right:
            stack.append((node.right, path + [node.right.val]))
        if node.left:
            stack.append((node.left, path + [node.left.val]))
    return []


def find_path2(root, target):
    if not root:
        return []
    path = []

    def dfs(node):
        if not node:
            return False
        path.append(node.val)
        if node.val == target:
            return True
        if dfs(node.left) or dfs(node.right):
            return True
        path.pop()
        return False
    if dfs(root):
        return path
    return []


def find_path3(root, target):

    def core(root, target):
        if root is None:
            return None

        if root.val == target:
            return [root.val]

        left_path = core(root.left, target)
        if left_path is not None:
            left_path.insert(0, root.val)
            return left_path

        right_path = core(root.right, target)
        if right_path is not None:
            right_path.insert(0, root.val)
            return right_path

        return None
    path = core(root, target)
    return path


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

path = find_path(root, 4)
print("到节点4的路径：", path)  # 输出路径 [1, 2, 4]
path = find_path2(root, 6)
print("到节点6的路径：", path)  # 输出路径 [1, 3, 6]
path = find_path3(root, 7)
print("到节点7的路径：", path)  # 输出路径 [1, 3, 7]

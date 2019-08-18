"""
面试题 7：重建二叉树
题目：输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输
入的前序遍历和中序遍历的结果中都不含重复的数字。例如输入前序遍历序列 {1,
2, 4, 7, 3, 5, 6, 8} 和中序遍历序列 {4, 7, 2, 1, 5, 3, 8, 6}，则重建出
图 2.6 所示的二叉树并输出它的头结点。


Leetcode: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def reconstruct_bianary_tree(preorder: [int], inorder: [int]) -> TreeNode:
    if not preorder or not inorder:
        return None
    if set(preorder) != set(inorder):
        return None
    root_index = inorder.index(preorder[0])
    root = TreeNode(preorder[0])
    root.left = reconstruct_bianary_tree(preorder[1: root_index+1], inorder[: root_index])
    root.right = reconstruct_bianary_tree(preorder[root_index+1: ], inorder[root_index+1: ])
    return root

def travel(tree: TreeNode, res: list):
    if tree:
        res.append(tree.val)
        travel(tree.left, res)
        travel(tree.right, res)


def bfs(tree: TreeNode):
    queue, res = [], []
    queue.append(tree)
    while queue:
        node = queue.pop(0)
        if not node:
            res.append("null")
            continue
        res.append(node.val)
        queue.append(node.left)
        queue.append(node.right)
    while res and res[-1] == "null":
        res.pop()
    return res


if __name__ == '__main__':
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    bt = reconstruct_bianary_tree(preorder, inorder)
    res = []
    travel(bt, res)
    print(res)
    bt = reconstruct_bianary_tree(preorder, inorder)
    res = bfs(bt)
    print(res)



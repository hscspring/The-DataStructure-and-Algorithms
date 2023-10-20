"""
二叉树中的 路径 被定义为一条节点序列，序列中每对相邻节点之间都存在一条边。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。

路径和 是路径中各节点值的总和。

给你一个二叉树的根节点 root ，返回其 最大路径和 。
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class MaxPathSum:

    def __init__(self):
        self.res = float("-inf")

    def max_path_sum(self, root):

        def core(root):
            if not root:
                return 0
            le = core(root.left)
            ri = core(root.right)

            add = root.val + le + ri
            if add > self.res:
                self.res = add
            return max(0, root.val + max(le, ri))

        core(root)
        return self.res


root = TreeNode(-10)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

ins = MaxPathSum()
res = ins.max_path_sum(root)
print(res)

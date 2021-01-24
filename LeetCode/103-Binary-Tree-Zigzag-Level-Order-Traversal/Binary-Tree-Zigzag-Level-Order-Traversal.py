# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Two stacks
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        stack1, stack2 = [], []
        stack1.append(root)
        while stack1 or stack2:
            tmp = []
            for i in range(len(stack1)):
                node = stack1.pop()
                tmp.append(node.val)
                if node.left:
                    stack2.append(node.left)
                if node.right:
                    stack2.append(node.right)
            if tmp:
                res.append(tmp)    
            tmp = []
            for i in range(len(stack2)):
                node = stack2.pop()
                tmp.append(node.val)
                if node.right:
                    stack1.append(node.right)
                if node.left:
                    stack1.append(node.left)
            if tmp:
                res.append(tmp)
        return res


# BFS + depth
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = []
        depth = 0
        queue.append(root)
        while queue:
            depth += 1
            tmp = []
            for i in range(len(queue)):
                node = queue.pop(0)
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if depth % 2 == 0:
                tmp.reverse()
            if tmp:
                res.append(tmp)
        return res
            
                
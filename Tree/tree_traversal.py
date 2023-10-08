import copy

from tree import TreeNode, connect_nodes


from traversal import (
    traversal_preorder_iteration2,
    traversal_preorder_iteration,
    traversal_preorder,
    traversal_postorder_iteration2,
    traversal_postorder_iteration,
    traversal_postorder,
    traversal_inorder_iteration,
    traversal_inorder,
    traversal_hierarchically,
    traversal_dfs,
    traversal_dfs_r,
    traversal_bfs,
)


tree = TreeNode(6)
connect_nodes(tree, TreeNode(4), TreeNode(9))
connect_nodes(tree.left, TreeNode(5), TreeNode(18))
connect_nodes(tree.right, None, TreeNode(26))
connect_nodes(tree.left.right, None, TreeNode(32))
connect_nodes(tree.right.right, TreeNode(12), None)
connect_nodes(tree.right.right.left, TreeNode(10), TreeNode(30))
connect_nodes(tree.right.right.left.right, TreeNode(8), TreeNode(45))
root = copy.deepcopy(tree)

# preorder
preorder_res = [6, 4, 5, 18, 32, 9, 26, 12, 10, 30, 8, 45]

# inorder
inorder_res = [5, 4, 18, 32, 6, 9, 10, 12, 8, 30, 45, 26]

# postorder
postorder_res = [5, 32, 18, 4, 10, 8, 45, 30, 12, 26, 9, 6]

print(preorder_res)
print(traversal_preorder(root), "preorder rec")
print(traversal_preorder_iteration(root), "preorder iter 1")
print(traversal_preorder_iteration2(root), "preorder iter 2")
print()
print(traversal_dfs(root), "dfs")
print(traversal_dfs_r(root), "dfs rec")
print(traversal_bfs(root), "bfs")
print(traversal_hierarchically(root), "hie")
print()
print(postorder_res)
print(traversal_postorder(root), "postorder rec")
print(traversal_postorder_iteration(root), "postorder iter 1")
print(traversal_postorder_iteration2(root), "postorder iter 2")

print(inorder_res)
print(traversal_inorder(root), "inorder rec")
print(traversal_inorder_iteration(root), "inorder iter")
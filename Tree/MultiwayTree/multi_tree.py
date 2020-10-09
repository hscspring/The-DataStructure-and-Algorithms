"""
@Yam 20190809
"""

class Node:
    def __init__(self, name: str):
        self.name = name
        self.children = []

class MultiTree:
    def __init__(self, root="/"):
        self.root = Node(root)

    def build(self, lst):
        for p in lst:
            # f is file or folder list
            f = p.split("/")
            pointer = self.root
            for i in range(1, len(f)):
                node = Node(f[i])
                if node not in pointer.children:
                    pointer.children.append(node)
                pointer = node
        return self.root

    def build_use_dict(self, lst):
        # self.children = {}
        for p in lst:
            f = p.split("/")
            pointer = self.root
            for i in range(1, len(f)):
                if f[i] not in pointer.children:
                    node = Node(f[i])
                    pointer.children[f[i]] = node
                    pointer = node
                else:
                    pointer = pointer.children[f[i]]
        return self.root

    @staticmethod
    def dfs_recursion(root):
        if len(root.children) == 0:
            return [root.name]
        children = root.children
        res = [root.name]
        for c in children:
            res.extend(MultiTree.dfs_recursion(c))
        return res

    @staticmethod
    def dfs(root):
        stack, res = [], []
        stack.append(root)
        while len(stack):
            curr = stack.pop()
            if curr.name not in res:
                res.append(curr.name)
            stack.extend(reversed(curr.children))
        return res

    @staticmethod
    def bfs(root):
        queue, res = [], []
        queue.append(root)
        while len(queue): 
            curr = queue.pop(0)
            # if curr.name not in res:
            res.append(curr.name)
            for child in curr.children:
                queue.append(child)
        return res

    @staticmethod
    def bfs_hierarchical(root):
        queue, res = [], []
        queue.append(root)
        while len(queue): 
            sub = []
            for i in range(len(queue)):
                curr = queue.pop(0)
                if curr.name not in sub:
                    sub.append(curr.name)
                queue.extend(curr.children)
            res.append(sub)
        return res

if __name__ == '__main__':
    paths = ['/2/2', '/2/2/7', '/2/3/5', '/a/b/c']
    tree = MultiTree()
    mt = tree.build(paths)

    print("DFS: ", tree.dfs(mt))
    print()
    print("BFS: ", tree.bfs(mt))
    print()
    print("BFS_hierarchical: ", tree.bfs_hierarchical(mt))
    print()
    print("DFS_recursion", tree.dfs_recursion(mt))

    # DFS:  ['/', '2', '3', '7', '5', 'a', 'b', 'c']
    # BFS:  ['/', '2', 'a', '3', 'b', '7', '5', 'c']
    # BFS_hierarchical:  [['/'], ['2', 'a'], ['3', 'b'], ['7', '5', 'c']]
    # DFS_recursion ['/', '2', '3', '7', '2', '3', '5', 'a', 'b', 'c']




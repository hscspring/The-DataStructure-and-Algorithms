"""
面试题 33：二叉搜索树的后序遍历序列
题目：输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。
"""

def verify_seq_bst(seq: list) -> bool:
    """
    Verify the given sequence is the Post-order traversal path of a bst.

    Parameters
    -----------
    seq: list
        the given list

    Returns
    ---------
    out: bool

    Notes
    ------

    """
    if not seq:
        return False
    root = seq[-1]
    length = len(seq)
    # 找到左子树（节点值小于 root）的 index
    i = 0
    for i in range(length):
        if seq[i] > root:
            break
    # 如果右子树节点的值小于 root
    j = i
    for j in range(i, length-1): # or length, because the last one is root, it doesn't matter.
        if seq[j] < root:
            return False

    left, right = True, True
    if i > 0:
        left = verify_seq_bst(seq[:i])
    if j < length - 1:
        right = verify_seq_bst(seq[j:-1])
    return left and right


def verify_seq_bst2(seq: list) -> bool:
    if not seq:
        return False
    
    l, r = True, True
    left, right = [], []
    root = seq[-1]
    length = len(seq)
    
    for i in range(length):
        if seq[i] < root:
            left.append(seq[i])
        else:
            break
    for j in range(i, length-1):
        if seq[j] > root:
            right.append(seq[j])
        else:
            return False
    
    if left:
        l = verify_seq_bst2(left)
    if right:
        r = verify_seq_bst2(right)

    return l and r


if __name__ == '__main__':
    lst = [5,7,6.9,11,10,8]
    lst = [7,4,6,5]
    # lst = [1,2,3,4,5]
    res = verify_seq_bst2(lst)
    print(res)
    




    
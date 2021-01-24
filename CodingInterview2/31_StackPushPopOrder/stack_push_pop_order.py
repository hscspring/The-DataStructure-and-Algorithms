"""
面试题 31：栈的压入、弹出序列
题目：输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是
否为该栈的弹出顺序。假设压入栈的所有数字均不相等。例如序列 1、2、3、4、
5 是某栈的压栈序列，序列 4、5、3、2、1 是该压栈序列对应的一个弹出序列，但
4、3、5、1、2 就不可能是该压栈序列的弹出序列。

"""



def is_pop_order(push_order: list, pop_order: list) -> bool:
    """
    Whether the pop order is for the push order.

    Parameters
    -----------
    push_order: list
    pop_order: list

    Returns
    ---------
    out: bool
        If the pop order is for the push order.

    Notes
    ------
    All the numbers are not the same.
    """
    if not push_order or not pop_order:
        return False
    stack = []
    for pop in pop_order:
        s_top = stack[-1] if stack else None
        if push_order and pop != s_top:# pop not in stack:
            x = push_order.pop(0)
            while x != pop:
                stack.append(x)
                if push_order:
                    x = push_order.pop(0)
                else:
                    return False
        else:
            if stack.pop() != pop:
                return False
    return True


def is_pop_order2(push_order, pop_order):
    if not push_order or not pop_order:
        return False
    stack = []
    for i in pop_order:
        if stack and stack[-1] == i:
            stack.pop()
        else:
            while push_order and push_order[0] != i:
                x = push_order.pop(0)
                stack.append(x)
            if push_order:
                push_order.pop(0)
            else:
                return False
    return True


if __name__ == '__main__':
    pass













    
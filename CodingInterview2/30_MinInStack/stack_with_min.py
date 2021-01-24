"""
面试题 30：包含 min 函数的栈
题目：定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min
函数。在该栈中，调用 min、push 及 pop 的时间复杂度都是 O (1)。

"""



class StackMin:

    """
    Stack with pop, push and min, all O(1).

    Parameters
    -----------

    Returns
    ---------

    Notes
    ------

    """
    def __init__(self):
        self.data_stack = []
        self.min_stack = []


    def pop(self):
        if not self.data_stack:
            return None
        x = self.data_stack.pop()
        if x == self.min_stack[-1]:
            self.min_stack.pop()
        return x

    def push(self, x):
        self.data_stack.append(x)
        if not self.min_stack or x < self.min_stack[-1]:
            self.min_stack.append(x)

    @property
    def min(self):
        if not self.min_stack:
            return None
        return self.min_stack[-1]




if __name__ == '__main__':
    st = StackMin()
    st.push(3)
    st.push(4)
    st.push(2)
    st.push(8)
    st.push(1)
    st.push(7)

    print(st.data_stack)
    print(st.min_stack)
    print(st.min)

    for i in range(6):
        print(st.pop())
        print(st.data_stack)
        print(st.min_stack)
        print(st.min)
        print("="*10)

    












    
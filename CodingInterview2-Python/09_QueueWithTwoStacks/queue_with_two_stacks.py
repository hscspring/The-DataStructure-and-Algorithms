"""
面试题 9：用两个栈实现队列
题目：用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail
和 deleteHead，分别完成在队列尾部插入结点和在队列头部删除结点的功能。
"""

class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def append(self, x):
        """
        Append from tail.
        """
        self.stack1.append(x)

    def delete(self):
        """
        Delete from head.
        """
        if len(self.stack2) == 0:
            while len(self.stack1):
                item = self.stack1.pop()
                self.stack2.append(item)
        if len(self.stack2) == 0:
            print("Queue empty.")
            return
        head = self.stack2.pop()
        return head


class Stack:
    def __init__(self):
        self.queue1 = []
        self.queue2 = []
    
    def append(self, x):
        self.queue1.append(x)
    
    def delete(self):
        if not self.queue2:
            while self.queue1:
                # 先进先出
                item = self.queue1.pop(0)
                self.queue2.append(item)
        if not self.queue2:
            return
        return self.queue2.pop()


if __name__ == '__main__':
    # que = Queue()
    stk = Stack()
    lst = [1, 2, 3, 4, 5]
    for i in lst:
        stk.append(i)
    x = stk.delete()
    print(x)










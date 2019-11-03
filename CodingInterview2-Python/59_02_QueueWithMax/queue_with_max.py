"""

面试题 59（二）：队列的最大值
题目：请定义一个队列并实现函数 max 得到队列的最大值，
要求函数 max，push_back pop_front 的时间复杂度都是 O(1)


"""


class QueueMax:

    def __init__(self):
        self.data = []
        self.maxes = []

    def push_back(self, x):
        while self.maxes and x >= self.maxes[-1]:
            self.maxes.pop()
        self.data.append(x)
        self.maxes.append(x)

    def pop_front(self):
        if not self.data:
            return None
        # x = self.data.pop(0)
        # if x == self.maxes[0]:
        #     self.maxes.pop(0)
        x = self.data[0]
        self.data = self.data[1:]
        if x == self.maxes[0]:
            self.maxes = self.maxes[1:]
        return x

    @property
    def max(self):
        if not self.maxes:
            return None
        return self.maxes[0]



if __name__ == '__main__':
    # lst = [2, 3, 4, 2, 6, 2, 5, 1]
    # qm = QueueMax()
    # for i in lst:
    #     qm.push_back(i)
    #     print(qm.data)
    #     print(qm.maxes)
    #     print(qm.max)
    #     print("="*10)

    # print("="*50)

    # for i in range(len(lst)):
    #     x = qm.pop_front()
    #     print(x)
    #     print(qm.data)
    #     print(qm.maxes)
    #     print(qm.max)
    #     print("="*10)

    qm = QueueMax()

    qm.push_back(4)
    qm.push_back(3)
    qm.push_back(2)
    qm.push_back(8)
    print(qm.data)
    print(qm.maxes)
    print(qm.max)
    print("="*10)

    qm.pop_front()
    qm.pop_front()
    qm.pop_front()
    print(qm.data)
    print(qm.maxes)
    print(qm.max)
    print("="*10)

    qm.push_back(6)
    qm.push_back(2)
    qm.push_back(5)
    print(qm.data)
    print(qm.maxes)
    print(qm.max)
    print("="*10)

    qm.pop_front()
    qm.pop_front()
    qm.pop_front()
    print(qm.data)
    print(qm.maxes)
    print(qm.max)
    print("="*10)

    qm.push_back(1)
    print(qm.data)
    print(qm.maxes)
    print(qm.max)
    print("="*10)













    
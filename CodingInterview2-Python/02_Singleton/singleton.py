# 面试题 2：实现 Singleton 模式
# 题目：设计一个类，我们只能生成该类的一个实例。


# 覆盖 new 方法
class Singleton1:

    _instance = None

    def __new__(cls):
        if cls._instance == None:
            cls._instance = object.__new__(cls)
        return cls._instance


# 元类
class MetaSingleton(type):
    # 通过继承元类中的 type 重写 init, call 创建新的 type
    def __init__(cls, *args):
        print(cls, "__init__ method called with args", args)
        type.__init__(cls, *args)
        cls.instance = None

    def __call__(cls, *args, **kwargs):
        if not cls.instance:
            print(cls, "creating instance", args, kwargs)
        return cls.instance


class Singleton2(metaclass=MetaSingleton):
    pass


# 共享状态（确保只有一个实例只是其中的一个方法）
class Borg:

    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state


class Singleton3(Borg):

    def __init__(self):
        Borg.__init__(self)
        self.state = "init"

    def __str__(self):
        return self.state


if __name__ == '__main__':
    # s1 = Singleton3()
    # s2 = Singleton3()
    # assert s1.state == s2.state
    # print(s1)
    # print(s2)

    class SingletonA(Singleton1):
        pass

    class SingletonB(Singleton1):
        pass

    class SingletonA1(SingletonA):
        pass
    a = SingletonA()
    a1 = SingletonA1()
    b = SingletonB()
    a.x = 100
    print(a.x)
    print(a1.x)
    print(b.x)

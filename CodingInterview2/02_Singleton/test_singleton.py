from singleton import Singleton1, Singleton2, Singleton3, Singleton4, Borg


def test1():
    s1 = Singleton1()
    s2 = Singleton1()
    assert s1 == s2


def test2():
    s1 = Singleton2()
    s2 = Singleton2()
    assert s1 == s2


def test3():
    s1 = Singleton3()
    s2 = Singleton3()
    s1.state = "hello"
    assert s2.state == s1.state


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


def test4():
    assert a1.x == a.x
    assert hasattr(a1, "x")
    assert not hasattr(b, "x")
    assert a == a1
    assert a != b


class SingletonC(Singleton2):
    pass


class SingletonD(Singleton2):
    pass


class SingletonC1(SingletonC):
    pass


c = SingletonC()
c1 = SingletonC1()
d = SingletonD()


def test5():
    assert c == c1
    assert c == d


class ABorg(Borg):
    pass


class BBorg(Borg):
    pass


class A1Borg(Borg):
    pass


e = ABorg()
e1 = A1Borg()
f = Borg()
e.x = 100


def test6():
    assert e.x == e1.x == 100
    assert e.x == f.x == 100


def test7():
    s = Singleton4()
    Singleton4.get_instance()
    s1 = Singleton4()
    s2 = Singleton4()
    assert s1.get_instance() == s2.get_instance()

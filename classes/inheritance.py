class MyError(Exception):
    pass


class B:
    def test(self):
        print('test from B')

    def __init__(self):
        print('B')


class C:
    def test(self):
        print('test from C')

    def __init__(self):
        print('C')


class D(B, C):                   # Multiple Inheritance
    def __init__(self):
        print('D')


class E(C, B):
    def __init__(self):
        print('E')

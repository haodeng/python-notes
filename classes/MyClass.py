class MyClass:
    i = 10

    @staticmethod
    def fun():
        print('fun')

    def fun2(self):
        print('fun2')

    def __init__(self):
        self.data = []


c = MyClass()
c.fun()
c.fun2()
print(c.i)


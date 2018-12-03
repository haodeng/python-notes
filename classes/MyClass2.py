class MyClass2:
    i = 10

    def __init__(self, i):
        self.i = i


c = MyClass2(5)
print(c.i)
d = MyClass2(2)
print(d.i)
print(c.i)


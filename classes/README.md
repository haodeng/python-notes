Scope

```python
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)


scope_test()
print("In global scope:", spam)
```

Result.  The nonlocal assignment changed scope_test’s binding of spam, and the global assignment changed the module-level binding.
```python
After local assignment: test spam
After nonlocal assignment: nonlocal spam
After global assignment: nonlocal spam
In global scope: global spam
```


```python
class MyClass:
    i = 10

    @staticmethod
    def fun():
        print('fun')

    def fun2(self):
        print('fun2')

    def __init__(self):        #class instantiation automatically invokes __init__() 
        self.data = []


c = MyClass()
c.fun()
c.fun2()
print(c.i)

Result:
fun
fun2
10
```

```python
class MyClass2:
    i = 10


    def __init__(self, i):
        self.i = i


c = MyClass2(5)
print(c.i)

Result:
5
```
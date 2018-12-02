Hanlding Exceptions

try-except equals to java try-catch
```python
>>> while True:
...   try:
...     x = int(input("Input a number:"))
...     break;
...   except ValueError:
...     print("Invalid number")
...
Input a number:kk
Invalid number
Input a number:2a
Invalid number
Input a number:12
```

```python
>>> from my_exceptions import *
>>> for cls in [B,C,D]:
...   try:
...     raise cls()
...   except D:
...     print('D')
...   except C:
...     print('C')
...   except B:
...     print('B')
...
B
C
D
```

The first matching exception is triggered
```python
>>> for cls in [B,C,D]:
...   try:
...     raise cls()
...   except B:
...     print('B')
...   except C:
...     print('C')
...   except D:
...     print('D')
...
B
B
B
```

except: catch unknown error, than reraise it.
```python
>>> import sys
>>> try:
...   1/0
... except ValueError:
...   print('Invalid Value')
... except:
...   print("Unknow error:", sys.exc_info()[0])
...   raise
...
Unknow error: <class 'ZeroDivisionError'>
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
ZeroDivisionError: division by zero
```

User-defined Exceptions
```python
class InputError(Exception):

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message
```

```python
>>> from input_error import *
>>> i = InputError('--d he', 'Invalid cmd')
>>> i
InputError('--d he', 'Invalid cmd')
```

try-except-else-finally

Finally and else are optional. Finally is always executed. Else is executed if no exceptions 
```python
>>> def div(x,y):
...   try:
...     r = x/y
...   except ZeroDivisionError:
...     print('division by zero')
...   else:
...     print("Result:", r)
...   finally:
...     print("quit")
...
>>> div(1,0)
division by zero
quit
>>> div(10,2)
Result: 5.0
quit
>>> div('a','b')
quit
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in div
TypeError: unsupported operand type(s) for /: 'str' and 'str'
```

```python
>>> def div(x,y):
...   try:
...     r = x/y
...     print('Result:',r)
...   except ZeroDivisionError:
...     print('division by zero')
...   finally:
...     print("quit")
...
>>> div(1,0)
division by zero
quit
>>> div(1,1)
Result: 1.0
quit
>>> div('d',9)
quit
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in div
TypeError: unsupported operand type(s) for /: 'str' and 'int'
```

Predefined Clean-up Actions

Use with is a good practice. file auto closed, like java try(closeable resources){}
```python
with open("myfile.txt") as f:
    for line in f:
        print(line)
```

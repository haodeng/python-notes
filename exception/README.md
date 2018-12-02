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


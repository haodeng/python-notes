# Data structure

List
```python
>>> L = [1,2,3]
>>> L.append(4)
>>> L
[1, 2, 3, 4]
>>> L.extend([5,6,7])
>>> L
[1, 2, 3, 4, 5, 6, 7]
>>> L.insert(0, 0)
>>> L
[0, 1, 2, 3, 4, 5, 6, 7]
>>> L.remove(0)
>>> L
[1, 2, 3, 4, 5, 6, 7]
>>> L.pop(3)
4
>>> L
[1, 2, 3, 5, 6, 7]
>>> L.index(7)
5
>>> L
[1, 2, 3, 5, 6, 7]
>>> L = [1,2,3,4,5,6,7]
>>> L
[1, 2, 3, 4, 5, 6, 7]
>>> L.pop(3)
4
>>> L
[1, 2, 3, 5, 6, 7]
>>> L.index(7)
5
>>> L.append(1)
>>> L
[1, 2, 3, 5, 6, 7, 1]
>>> L.count(1)
2
>>> L.reverse()
>>> L
[1, 7, 6, 5, 3, 2, 1]
>>> L.sort()
>>> L
[1, 1, 2, 3, 5, 6, 7]
>>> L.sort(reverse = True)
>>> L
[7, 6, 5, 3, 2, 1, 1]
>>> L1 = L.copy()
>>> L1
[7, 6, 5, 3, 2, 1, 1]
>>> L.clear()
>>> L
[]
>>> L1
[7, 6, 5, 3, 2, 1, 1]

```


Use List as Stack (last in, first out)

```python
>>> stack = [1,2,3]
>>> stack.append(4)
>>> stack.append(5)
>>> stack
[1, 2, 3, 4, 5]
>>> stack.pop()          # pop out the last one 
5
>>> stack
[1, 2, 3, 4]
>>> stack.pop()
4
>>> stack
[1, 2, 3]
```

Use List as Queue (first in, first out)

Doing insert and pop from the beginning of a list is slow, so we use collections.deque which take List and support popleft()
```python
>>> from collections import deque
>>> queue = deque([1, 2, 3])
>>> queue
deque([1, 2, 3])
>>> queue.append(4)
>>> queue
deque([1, 2, 3, 4])
>>> queue.popleft()
1
>>> queue
deque([2, 3, 4])
```

List Comprehensions, a concise way to create a list
```python
>>> squares = list(map(lambda x: x**2, range(10)))
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> squares = [x**2 for x in range(10)]   # This one is more readable
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

More examples
```python
>>> [(x,y) for x in [1,2,3] for y in [2,3,4] if x != y]
[(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 2), (3, 4)]

>>> [y*2 for y in x]
[2, 4, 6, 8]
>>> [y*2 for y in x if y*2>5]
[6, 8]
>>> strs = ['  a ', 'b  ', ' c ']
>>> [s.strip() for s in strs]
['a', 'b', 'c']
>>> [(x, x**2) for x in [1,2,3,4,5]]    # create a list of 2-tuples
[(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
```


Del 
```python
>>> l = [1,2,3,4,5,6]
>>> del l[0]
>>> l
[2, 3, 4, 5, 6]
>>> del l[2:4]
>>> l
[2, 3, 6]
>>> del l[:]
>>> l
[]
>>> del l
>>> l
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'l' is not defined
```


Tuple
```python
>>> t = 1,2,3,'a', 3.45
>>> t
(1, 2, 3, 'a', 3.45)
>>> t[1]
2
>>> t1 = 'zero', t          #Tuple can be nested
>>> t1
('zero', (1, 2, 3, 'a', 3.45))
>>> t[0] = 0                #Tuple is immutable
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
```

```python
>>> t2 = (2,3,4, 'str')
>>> t2
(2, 3, 4, 'str')
>>> t3 = ([1,3], [3,4,5], 'a')
>>> t3
([1, 3], [3, 4, 5], 'a')
>>> empty = ()
>>> empty
()
>>> len(empty)
0
```

Sequence unpacking. It works for any sequence on the right-hand side. 
```python
>>> t = 'a', 2, 'b', 3       # packing
>>> v1, v2, v3, v4 = t       # unpacking
>>> v1
'a'
>>> v2
2
>>> v3
'b'
>>> v4
3
```

Set, use {} or Set() to create new set
```python
>>> s = set([1,2,3,4])
>>> s
{1, 2, 3, 4}
>>> s2 = {1,2,3,4}
>>> s2
{1, 2, 3, 4}
>>> s3 = set('abababababa')
>>> s3
{'b', 'a'}         # duplications removed
```

Set operations -, &, |, ^
```python
>>> s1 = set('abcdef')
>>> s2 = set('abcx')
>>> s1 - s2          # In s1, but not in s2
{'f', 'd', 'e'}
>>> s1 + s2          # + not support
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'set' and 'set'
>>> s1 | s2            # In s1 or s2, or both
{'b', 'x', 'e', 'a', 'c', 'f', 'd'}
>>> s1 & s2           # In both s1 and s2
{'c', 'b', 'a'}
>>> s1 ^ s2           # In s1 or s2, not in both
{'e', 'd', 'f', 'x'}
```

set comprehensions
```python
>>> s = {x for x in set('abababcdefjkdjugjq') if x >'d'}
>>> s
{'e', 'g', 'q', 'k', 'f', 'u', 'j'}
```

Dictionary, equls to java map
```python
>>> dic = {'a':'A', 'b':'B'}
>>> dic['c'] = 'C'
>>> dic
{'a': 'A', 'b': 'B', 'c': 'C'}
>>> dic['a']
'A'
>>> del dic['a']
>>> dic
{'b': 'B', 'c': 'C'}
>>> list(dic)          # A list of dic keys
['b', 'c']
>>> 'b' in dic
True
>>> 'k' not in dic
True
>>> sorted(dic, reverse=True)
['c', 'b']
```

```python
>>> {x: x**2 for x in range(10)}
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
>>> {x: x+y for x, y in zip(range(10), range(10))}
{0: 0, 1: 2, 2: 4, 3: 6, 4: 8, 5: 10, 6: 12, 7: 14, 8: 16, 9: 18}
>>> dic = dict(a='A', b='B', c='C')
>>> dic
{'a': 'A', 'b': 'B', 'c': 'C'}
```

Looping
```python
>>> dic
{'a': 'A', 'b': 'B', 'c': 'C'}
>>> for k,v in dic.items():
...   print(k,v)
...
a A
b B
c C

>>> L
[1, 2, 3]
>>> for v in L:
...   print(v)
...
1
2
3
>>> for i, v in enumerate(L):     # i is the position index
...   print(i, v)
...
0 1
1 2
2 3
```

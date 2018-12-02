Import Module

```python
# greeting.py

def greeting(name):
    print("Hello, ", name)
```

```python
>>> import greeting
>>> greeting.greeting('Hao')
Hello,  Hao
```
```python
>>> import greeting as g
>>> g.greeting('Hao')
Hello,  Hao
```
```python
>>> from greeting import greeting  # Import only greeting function
>>> greeting('Hao')
Hello,  Hao
```
```python
>>> from greeting import *          # Import all functions
>>> greeting('Hao')
Hello,  Hao
```
```python
>>> from greeting import greeting as greeting_me   # Import and renmae function
>>> greeting_me('me')
Hello,  me
```

Reload a module

A module is only loaded once it is imported, any changes can use importlib to reload.
```python
>>> import importlib
>>> importlib.reload(importlib.import_module('greeting'))
<module 'greeting' from 'C:\\hao\\examples\\python-notes\\modules\\greeting.py'>
>>> from greeting import *
>>> greeting('Hao')
Hi, there, hello,  Hao
```

Executing modules as scripts

Add __name__ set to "__main__" to the end of the module

```python
# greeting.py
def greeting(name):
    print("Hi, ", name)


if __name__ == "__main__":
    import sys
    greeting(sys.argv[1])
```

Run script
```python
python greeting.py 'Hao'
Hi,  'Hao'
```


Standard Modules
```python
>>> import sys
>>> sys
<module 'sys' (built-in)>
>>> sys.path
['', 'C:\\Users\\hao\....]

>>> import greeting
>>> dir(greeting)
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'greeting']
>>> dir()            # current dir
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'greeting', 'sys']
>>>
```

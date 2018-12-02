Package

__init__.py files are required to make Python treat the directories as containing packages. Package structure:

```javascript
testpackage/                          Top-level package
      __init__.py                     Initialize the testpackage
      subpackage/                     Subpackage
              __init__.py
              test.py
```


Import a package
```python
>>> import testpackage.subpackage.test
>>> testpackage.subpackage.test.test()
test
```

```python
>>> from testpackage.subpackage import test
>>> test.test()
test
```

```python
>>> from testpackage.subpackage.test import test
>>> test()
test
```
```python
>>> from testpackage.subpackage.test import *   # Import all functions of test.py
>>> test()
test
>>> test_v2()
test v2
```

"from testpackage.subpackage.test import *" Equals to:
```python
>>> from testpackage.subpackage.test import test
>>> from testpackage.subpackage.test import test_v2
```

# PowerPy
Powerpy is a collection of small functions and classes for Python3, contains an implementation of common patterns and other simple functions to make your life a bit easier.

## Installation
The package can be installed through pip:

    $ pip install powerpy

or downloaded from [GitHub](https://github.com/jacopodl/powerpy).

## Examples
To implement a simple type checking in your classes:
```python
from powerpy.type_checking import EnsureTypes

class Test(EnsureTypes):
    def __init__(self):
        self.prop1 = ""
        self.prop2 = 123
        self.prop3 = None

t=Test()
t.prop1="Hello" # OK
t.prop1=123 # Error
t.prop3 = "World" # OK
t.prop3 = 123 # Ok
```
Partial application:
```python
from powerpy.currying import Currying

@Currying
def simple_func(param1, param2):
    return param1 + param2

s1 = simple_func("Hello")
print(s1("Alice")) # HelloAlice
print(s1("Bob")) # HelloBob
```


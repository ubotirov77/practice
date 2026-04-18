'''OBJECTS 
(1) Whats object
(2) Iterable objrcts and range
(3) Dictionary 
(4) Error handling system
'''

import array  # package/module
import math
from math import ceil, asin
print("=====  Whats object ======")
# An object has state and method properties
# Everything is object in python

print(type("Hello World"))
print(type(100))
print(type(True))
print(type(array))
print(type(math))

# Paradigm > Functional Programming & OOP
# OOP 4 concepts > Abstraction | Encapsulation | Inheritence | Polymorphism
result = math.ceil(97.7)  # call
print("result", result)

result2 = ceil(98.7)
print("result2:", result2)

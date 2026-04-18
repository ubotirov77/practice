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


print("===== Error handling system ======")
car_dict = dict(name="Toyoto", year=2026, electric=True)

try:
    print("passed here")
    a = car_dict.speed
    result_car = car_dict["origin"]
    print("result_car", result_car)
except KeyError as err:
    print("No origin state found:", err)
except AttributeError as err:
    print("No speed found:", err)
else:
    print("Exercuted succsessfully without errors")
finally:
    print("Final crossing logic")

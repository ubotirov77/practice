''' Operators and conditions 
(1) Operators
(2) Conditions 
(3) Logical Operators
'''
print("==== Operators ====")
# + - > >= < <= == is  */      // % += **

a = 19
b = 5
print(a/b)
result = a // b
left = a % b
print(f"the result {result}, and left {left}")
# a= a+ 100
a += 100
print("a:", a)

print("b*b:", b**2)
print("b**3:", b**3)
print("="*10)

c = dict(name="Norman", age=24)
d = dict(name="Norman", age=24)
e = c
print("c == d", c == d)  # only value compared
print(id(c), id(d))

data = c is d
print("c is d", data)
print("c is e", c is e)
print(id(c), id(e))

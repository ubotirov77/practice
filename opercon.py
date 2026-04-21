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

'''==============================================================================================================
------------------------------------------------ Conditions ---------------------------------------------------
================================================================================================================='''
print("==== Conditions ====")

x = 5
if x > 50:
    print("Case A")
elif x > 10:
    print("Case B")
else:
    print("Case C")


print("==== Logical Conditions ====")

age = 21
# person = None

# if age >= 18:
#     person = "Teenage"
# elif age >= 25:
#     person = "Adult"
# else:
#     person = "Child"
# print("person:", person)

# Ternary
person = "Adult" if age > 18 else "minor"
print("person is:", person)

print("-----------------")
is_student = True
is_admin = False
is_guest = True
is_parent = False

if not is_student:
    print("Wellcome here do you want to become student!")
elif is_admin:
    print("Please go to office")
elif is_guest or is_parent:
    print("Waiting room is over there↗️")
else:
    print("ETC")

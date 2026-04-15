''' FUNCTION
(1) Define vs Call
(2) Parametr vs Argument
(3) Keyword & default arguments
(4) Scope

'''

print("===== Define(parametr) vs Call(argument) =====")
# built in function > print() type()
# Function - reusable block of code
# Instead of block{} in JAVA, Python uses indentation!

# define - parametr


def greet(a):
    print(f"How do you do, {a}")


def greeting(b):
    print("greeting is executed")
    return f"Hi {b}"


# call - argument
result = greet("Norman")
print("result:", result)

result2 = greeting("Justin")
print("result2:", result2)

print("=====  Keyword & default arguments =====")


# define
def give_greet(name, age=24):
    print("give_greet is executed")
    return f"Hi {name}, you are {age} years old"


# call
result3 = give_greet(name="Norman", age=23)
print("result3:", result3)

result4 = give_greet(name="Daniel")
print("result3:", result4)

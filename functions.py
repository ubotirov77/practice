''' FUNCTION
(1) Define vs Call
(2) Parametr vs Argument
(3) Keyword & default arguments

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

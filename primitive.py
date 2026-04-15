print("===== number ======")
# in JAVA, variable is a name of storage location
# in PYTHON, variable is named reference

count = 100
count_type = type(count)
print(f"the count{count} and type of count: {count_type}")

result1 = count.bit_count()  # method
result2 = count.numerator  # state
print(result1, result2)

print("===== string ======")
# METHODS: upper() lower() title() find() replace()

course = "AI Python FullStack"
result = type(course)
print(f"the type of course:{result}")

result = course.title()
print(f"the result 1: {result}")

result = course.upper()
print(f"the result 2: {result}")

result = course.replace("FullStack", "MasterClass")
print(f"the result 2: {result}")
print(course)

print("===== boolean ======")
# funtions > type() input() int() str()
y = input("give your value for y:")
print("value of y:", y)

result = y.isnumeric()
print(f"the input is numeric {result}")

# TRUTHY vs FALSY value
# TRUTH : True 100 -100 "MIT"
# FALSY : False 0 "" None

test_falsy = "" or False or None or 0
print("the FALSY:", bool(test_falsy))

test_truthy = "MIT"
print("the TRUTHY:", bool(test_truthy))

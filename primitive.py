print("===== number ======")
# in JAVA, variable is a name of storage location
# in PYTHON, variable is named reference

count = 100
count_type = type(count)
print(f"the count{count} and type of count: {count_type}")

result1 = count.bit_count()  # method
result2 = count.numerator  # state
print(result1, result2)

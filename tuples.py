''' Tuple
(1) whats tuplr: tuple vs list
(2) unpacking arguments
(3) zip
'''

print("===== whats tuplr: tuple vs list ======")
# Java/Php/Node.js arrays => python list

# literal
numbs = [3, 5, 1, 2]
print(numbs)

# constructor
letters = list("hello world!")
print(letters)

fruits = ["apple", "lemon", "banana", "kivi"]
print("before fruits", fruits)

fruits[2] = "melon"
print("after fruits", fruits)

# tuple we can't mutate 
animals = ("dog", "cat", "fish", "lion")
tuple_obj = ("MIT", 100, True, None)

print(animals[0])
animals[0] = "bird"

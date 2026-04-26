'''List 
(1) Working with lists 
(2) List methods
(3) lambda function
(4) enumarate , map, filter
'''

print("===== Working with lists ======")
# Java/PHP/NODE.js array => python list

# literal
person = {"name": "Justin", "age": 25}  # dictinary
people = ("Andrew", "John", "Norman")  # tuple
groups = ["MIT", "Flexy", "Devex", "MG"]
for team in groups:
    print("The team :", team)


# constructor
result = list("Hello World!")
print(f"the result: {result} and size: {len(result)}")


print("-------------")
fruits = ["apple", "orange", "lemon", "kiwi"]

a = fruits[0]
b = fruits[0:2]
c = fruits[::3]
d = fruits[::-1]

print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)

print("===== List methods ======")
# methods > append() insert() pop() remove() clear() sort() index()

letters = ["a", "d", "b"]
print("the letters before:", letters)

letters.append("c")  # add behind
print("the letters after:", letters)

letters.insert(0, "z")  # add front
print("the letters after:", letters)

size = len(letters) - 1
result1 = letters.pop(size)  # pop behind
print(f"the pop result : {result1} and letters: {letters}")

result2 = letters.pop(0)  # pop front
print(f"the popped result2 : {result2} and letters: {letters}")


print("--------")
animals = ["dog", "cat", "capybara", "fish", "lion"]
print("animals:", animals)

result3 = animals.remove("lion")
print("Animals:", animals)

del animals[2:4]
print("animals delete:", animals)

exist = animals.index("cat")
print("animal inxex:", exist)

animals.clear()
print("animals:", animals)

if "cat" in animals:
    print("index of cat", animals.index("cat"))
else:
    print("cat does not exist")

print("------------")
numbers = [2, 28, 12, 8, 57]
numbers.sort()
print("sort default:", numbers)
numbers.sort(reverse=True)
print("sort reverse:", numbers)

# immutable > sorted & index
numbs = [2, 20, 12, 100]
new_numbs = sorted(numbs)
print(f"numbs:{numbs} and new numbs: {new_numbs}")


print("===== lambda function ======")
# lambda is small anonymous function:
def calculate(x, y): return x * y


result = calculate(3, 5)
print("result", result)

people1 = [
    ("Robert", 20),
    ("Steeve", 19),
    ("Joseph", 25),
    ("Norman", 27),
    ("Ali", 40)
]
people1.sort()
print("people :", people1)
# sort by age via lambda
people1.sort(key=lambda person: person[1])
print("people :", people1)

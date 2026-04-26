# ''' Tuple
# (1) whats tuplr: tuple vs list
# (2) unpacking arguments
# (3) zip
# '''

# print("===== whats tuplr: tuple vs list ======")
# # Java/Php/Node.js arrays => python list

# # literal
# numbs = [3, 5, 1, 2]
# print(numbs)

# # constructor
# letters = list("hello world!")
# print(letters)

# fruits = ["apple", "lemon", "banana", "kivi"]
# print("before fruits", fruits)

# fruits[2] = "melon"
# print("after fruits", fruits)

# # tuple we can't mutate
# animals = ("dog", "cat", "fish", "lion")
# tuple_obj = ("MIT", 100, True, None)

# print(animals[0])
# # animals[0] = "bird"
# # try avoid these ⬇️
# people = "Andrew", "John"
# amimals = "dog",


# print("===== unpacking arguments ======")

# groups = ["MIT", "FLEXY", "DEVEX", "MG"]

# (x, y, *z) = groups
# print(f"the x: {x} and y: {y} ")
# print("z:", z)

# # * args > tuples


# def calculate(*args):
#     print("*args >", args)
#     total = 1
#     for x in args:
#         total *= x
#     print(f"the total value : {total}")
#     return total


# # call
# calculate(1, 7, 2, 3)
# print('----------')
# calculate(0, 2, 300)
# print('----------')
# calculate(5, 7)

# # **kwargs > dictionary


# def introduce(**kwargs):
#     print(f"the type(**kwags) value: {type(kwargs)}")
#     print(f" Hi, I am {kwargs["name"]} and I am {kwargs["age"]} years old")
#     pass


# # call
# introduce(name="Norman", age=23)
# introduce(name="Shawn", age=32, single=True)


# def greeting(*args, **kwargs):
#     print("*args", args)
#     print("**kwargs", kwargs)


# # call
# greeting("hi", True, 10, name="John", age=22)

# print("===== zip ======")

# tuple1 = (1, 2, 3, 4)
# tuple2 = ("a", "b", "c")

# zipped = zip(tuple1, tuple2)
# print("zipped:", zipped)
# result = list(zipped)
# print("result", result)

a = 10
a =20
print(a)

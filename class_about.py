'''Class
(1) What is Class
(2) ordinary vs statistic properties
(3) special methods
'''

print("===== What is Class =====")
# class - object yasovchi shablon
# structure > state constructor method


class Person():
    # state
    message = "class state property"

    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # method
    def introduce(self):
        print(f"{self.name} says: How do you do!")

    def say_age(self):
        print(f"{self.name} says: I am {self.age}!")

    @classmethod
    def explain(cls):
        print("static method property executed!")


person1 = Person("Norman", 23)
person2 = Person("Daniel", 24)
person3 = Person("Justin", 28)

# ordinary state
print("person1 name:", person1)

# ordinary
person1.introduce()
person2.say_age()

print("===== ordinary vs statistic properties =====")
# static state
new_message = Person.message
print("new message:", new_message)


# static method
Person.explain()

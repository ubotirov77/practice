''' CLASS deep diving
(1) Encapsulation
(2) Inheriteance
(3) Polymorphism
'''
print("==== Inheritence ====")
# Parent > child
# Parent only inherit its public and protected properties to children


class Animal:

    description = f"This class parent for animals"

    def __init__(self, voice):
        self.voice = voice
        self._status = "the  animal is alive"

    def make_voice(self):
        print(f"the animal can make voice:{self.voice}")


class Dog(Animal):

    def __init__(self, name, sound, voice):
        super().__init__(voice)
        self.name = name
        self.sound = sound

    def introduce(self):
        print(f"{self.name} says: {self.sound}{self.sound}")

    def protect(self):
        print("yes I can protect you", self.sound, self.sound)

    def make_voice(self):
        print(f"the {self.name} can make sound {self.sound}")


class Cat(Animal):

    def __init__(self, name, sound, voice):
        super().__init__(voice)
        self.name = name
        self.sound = sound

    def introduce(self):
        print(f"{self.name} says: {self.sound}{self.sound}")

    def play(self):
        print(f"I am {self.name} I love playing {self.sound}")


class Fish(Animal):

    def __init__(self, name, sound, voice):
        super().__init__(voice)
        self.name = name
        self.sound = sound

    def introduce(self):
        print(f"{self.name} says: {self.sound}{self.sound}")

    def seek(self):
        print(
            f"men dadamni qidirib yuribman ko'rdadingizmi {self.sound} {self.sound}")


dog = Dog("Rex🦮", "woof🔊", True)
cat = Cat("Tom🐈", "meow🔊", True)
fish = Fish("Nemo🐟", "💤", False)
dog.introduce()
cat.introduce()
fish.introduce()

print("------------------")
dog.make_voice()
fish.make_voice()
print("------")
print(Dog.description)
print("status:", dog._status)
print("status:", cat._status)
print("status:", fish._status)

'''==============================================================================================================
------------------------------------------------ POLYMORPHISM ---------------------------------------------------
================================================================================================================='''
print("==== POLYMORPHISM ====")
dog.make_voice()
fish.make_voice()

print("-----")
# fish > Fish > Animal > object
a = isinstance(fish, Fish)
b = isinstance(fish, Animal)
c = isinstance(fish, object)
d = isinstance("MIT", object)
result = a and b and c and d
print("result:", result)
# Fish > Animal > object
data = issubclass(Fish, Animal)
data2 = issubclass(Animal, object)
print("data", data, data2)

'''
Museum ticket machine
'''


def muzey_ticket():
    print("Assalomu Alaykum Amir Temur muzeyiga xush kelibsiz")

    name = input("Iltimos ismingizni kiriting: ")
    age = int(input(f"{name.title()}, yoshingizni kiriting: "))

    if age >= 65:
        print(f"{name.title()}, siz uchun bepul")
    elif age >= 18:
        print(f"{name.title()}, siz uchun bilet narxi 40$")
    elif age >= 12:
        print(f"{name.title()}, siz uchun bilet narxi 25$")
    elif age >= 5:
        print(f"{name.title()}, siz uchun bilet narxi 10$")
    else:
        print(f"{name.title()}, siz uchun bepul")


muzey_ticket()

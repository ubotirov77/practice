# '''
# Museum ticket machine
# '''


# def muzey_ticket():
#     print("Assalomu Alaykum Amir Temur muzeyiga xush kelibsiz")

#     name = input("Iltimos ismingizni kiriting: ")
#     age = int(input(f"{name.title()}, yoshingizni kiriting: "))

#     if age >= 65:
#         print(f"{name.title()}, siz uchun bepul")
#     elif age >= 18:
#         print(f"{name.title()}, siz uchun bilet narxi 40$")
#     elif age >= 12:
#         print(f"{name.title()}, siz uchun bilet narxi 25$")
#     elif age >= 5:
#         print(f"{name.title()}, siz uchun bilet narxi 10$")
#     else:
#         print(f"{name.title()}, siz uchun bepul")


# muzey_ticket()

def atm():
    balance = 0
    password = 1234
    name = input("hello whats your name ")
    pin = int(input(f"hello {name.title()} insert your password"))
    if pin != password:
        int(input("your password is not matched try again"))
        if pin != password:
            print("your card is blocked")
        else:
            pass

    else:
        print(f"welcome {name.title()} to our atm")
        option = int(
            input("select service: for view balance enter 1 for deposit enter 2"))
        if option == 1:
            print(f"{name} your balance is {balance} usd")
        elif option == 2:
            deposit = int(input("enter amount you want to deposit"))
            balance = deposit + balance
            print(f"{deposit}usd deposited. your current balsace {balance} usd ")


atm()

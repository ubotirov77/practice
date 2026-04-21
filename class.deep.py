''' CLASS deep diving
(1) Encapsulation
(2) Inheriteance
(3) Polymorphism
'''
print("===== Encapsulation =====")
'''
c++ java > public private protected
php typeScript > public private protected
Python > name __private _protected
'''


class Account():
    # static
    description = "The class makes bank accounts"

    # constructor
    def __init__(self, owner, amount):
        self.__owner = owner
        self.__amount = amount

    # method
    def get_balance(self):
        print(f"the owner {self.__owner} has {self.__amount} usd")

    def deposit(self, amount):
        self.__amount += amount
        print(f"{amount}usd has been deposited. Current balance :{self.__amount}usd")

    def withdraw(self, amount):
        self.__amount -= amount
        print(f"{amount}usd has been withdrawed. Current balance {self.__amount}usd")

    @property
    def holder(self):
        return self.__owner

    @holder.setter
    def holder(self, new_owner):
        self.__owner = new_owner

    def change_ownership(self, new_owner):
        self.__owner = new_owner
        print("change ownership", new_owner)


my_account = Account("Norman", 1000)
my_account.get_balance()

print("-----------------")
my_account.deposit(3500)
my_account.withdraw(500)
my_account.get_balance()

# my_account.amount = 10000000
my_account.get_balance()

print("-----------------")
try:
    result = my_account.__amount
    print("result:", result)
except Exception as err:
    print("no target state found", err)

# getter vs setter
print("owner before:", my_account.holder)

# my_account.change_ownership("Daniel")
my_account.holder = "Daniel"
print("owner after:", my_account.holder)
my_account.get_balance()

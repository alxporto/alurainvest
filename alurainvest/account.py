
class Account:
    def __init__(self, id, owner, balance, limit):
        print(f"Building the object...{self}")
        self.__id = id
        self.__owner= owner
        self.__balance = balance
        self.__limit = limit

def statement(self):
    print(f"Balance of {self.__balance:.2f} from {self.__owner}")

def deposit(self, value):
    self.__balance += value

def withdraw(self, value):
    self.__balance -= value

def transfer(self, value, recipient):
    self.withdraw(value)
    recipient.deposit(value)

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

    def __could_withdraw(self, value):
        available_value = (self.__balance + self.__limit)
        return value <= available_value

    def withdraw(self, value):
        if self.__could_withdraw(value):
            self.__balance -= value
        else:
            print(f"The value {value} exceeded the limit")

    def transfer(self, value, recipient):
        self.withdraw(value)
        recipient.deposit(value)

    @property
    def balance(self):
        return self.__balance

    @property
    def owner(self):
        return self.__owner

    @property
    def limit(self):
        return self.__limit
    
    @limit.setter
    def limit(self, limit):
        self.__limit = limit
    
    @staticmethod
    def bank_code():
        return "001"
    
    @staticmethod
    def bank_codes():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}
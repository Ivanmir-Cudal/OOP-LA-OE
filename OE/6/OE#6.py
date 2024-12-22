class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance
       
    def deposit(self, ammount):
        if num > 0:
            self.__balance += ammount
        else:
            return "invalid"
    def withdraw(self, ammount):
        if self.__balance > ammount:
            self.__balance -= ammount
        else:
            return "invalid"
    def display_account_info(self):
        print(f"your account number is: {self.__account_number} and current balance is: {elf.__balance}")
    def may_pera_ba(self):
        return self

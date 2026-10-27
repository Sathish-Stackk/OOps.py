class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def show_balance(self):
        print(self.name, "Balance: ₹", self.__balance)

account = BankAccount("Sathish", 5000)
account.deposit(1500)
account.show_balance()

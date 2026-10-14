class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance


account = BankAccount("Sathish", 5000)

account.deposit(1500)
account.withdraw(1000)

print("Account Holder:", account.owner)
print("Balance:", account.get_balance())

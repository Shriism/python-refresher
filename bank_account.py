class BankAccount:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def get_balance(self):
        return self.balance

    def withdraw(self, amount):
        if amount < self.balance() or amount > 0:
            self.balance -= amount

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
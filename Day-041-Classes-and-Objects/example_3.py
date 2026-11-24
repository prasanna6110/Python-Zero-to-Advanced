# Day 041 · Classes and Objects — Modelling a real thing: BankAccount
# Run: python example_3.py

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.history = []

    def deposit(self, amount):
        self.balance += amount
        self.history.append(("deposit", amount))

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
            return
        self.balance -= amount
        self.history.append(("withdraw", amount))

acc = BankAccount("Prasanna", 1000)
acc.deposit(500)
acc.withdraw(2000)
acc.withdraw(300)
print(acc.owner, acc.balance, acc.history)

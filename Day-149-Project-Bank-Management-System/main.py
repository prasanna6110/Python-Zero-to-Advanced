# Day 149 · Project: Bank Management System — Bank Management System
# Run: python main.py

import hashlib
import json
import sys
from abc import ABC, abstractmethod
from datetime import datetime
from pathlib import Path

DEMO = not sys.stdin.isatty()

class BankError(Exception): pass
class InsufficientFunds(BankError): pass
class AuthError(BankError): pass

def hash_pin(pin):
    return hashlib.sha256(f"salt-{pin}".encode()).hexdigest()

class Account(ABC):
    _next_no = 1001
    def __init__(self, owner, pin, balance=0.0, number=None, history=None):
        self.owner = owner
        self.number = number or Account._next_no
        Account._next_no = max(Account._next_no, self.number) + 1
        self._pin = pin if len(str(pin)) == 64 else hash_pin(pin)
        self._balance = balance
        self.history = history or []

    @property
    def balance(self):
        return self._balance

    def check_pin(self, pin):
        if hash_pin(pin) != self._pin:
            raise AuthError("wrong PIN")

    def _log(self, kind, amount):
        self.history.append({"time": datetime.now().strftime("%d-%m %H:%M"), "type": kind,
                             "amount": amount, "balance": round(self._balance, 2)})

    def deposit(self, amount):
        if amount <= 0:
            raise BankError("amount must be positive")
        self._balance += amount
        self._log("DEPOSIT", amount)

    def withdraw(self, amount):
        if amount > self._balance - self.min_balance():
            raise InsufficientFunds(f"available ₹{self._balance - self.min_balance():.2f}")
        self._balance -= amount
        self._log("WITHDRAW", amount)

    @abstractmethod
    def min_balance(self): ...

    def to_dict(self):
        return {"type": type(self).__name__, "owner": self.owner, "pin": self._pin,
                "balance": self._balance, "number": self.number, "history": self.history}

class Savings(Account):
    RATE = 0.035
    def min_balance(self): return 1000
    def add_interest(self):
        interest = round(self._balance * self.RATE / 12, 2)
        self._balance += interest
        self._log("INTEREST", interest)

class Current(Account):
    def min_balance(self): return -5000          # overdraft allowed

class Bank:
    TYPES = {"Savings": Savings, "Current": Current}
    def __init__(self, path):
        self.path, self.accounts = path, {}
        if path.exists():
            for d in json.loads(path.read_text()):
                cls = self.TYPES[d.pop("type")]
                acc = cls(**d)
                self.accounts[acc.number] = acc
    def open(self, cls, owner, pin, deposit):
        acc = cls(owner, pin)
        acc.deposit(deposit)
        self.accounts[acc.number] = acc
        self.save()
        return acc
    def transfer(self, src, dst, amount, pin):
        src.check_pin(pin)
        src.withdraw(amount)
        dst.deposit(amount)
        self.save()
    def save(self):
        self.path.write_text(json.dumps([a.to_dict() for a in self.accounts.values()], indent=1))

def statement(acc):
    print(f"\n📄 Mini statement: {acc.owner} (A/C {acc.number}, {type(acc).__name__})")
    for h in acc.history[-5:]:
        print(f"   {h['time']}  {h['type']:<9} ₹{h['amount']:>10,.2f}   bal ₹{h['balance']:>10,.2f}")
    print(f"   Available balance: ₹{acc.balance:,.2f}")

def demo(bank):
    a = bank.open(Savings, "Prasanna", 1234, 15000)
    b = bank.open(Current, "Asha", 4321, 2000)
    a.withdraw(2500)
    bank.transfer(a, b, 5000, 1234)
    b.withdraw(6500)                              # uses the overdraft
    a.add_interest()
    for action in [lambda: a.withdraw(50000), lambda: bank.transfer(a, b, 10, 9999), lambda: a.deposit(-5)]:
        try:
            action()
        except BankError as e:
            print(f"❌ {type(e).__name__}: {e}")
    statement(a); statement(b)

def interactive(bank):
    while True:
        print("\n🏦 1.Open account 2.Deposit 3.Withdraw 4.Transfer 5.Statement 0.Exit")
        c = input("> ")
        try:
            if c == "1":
                cls = Savings if input("Type (s=savings / c=current): ") == "s" else Current
                acc = bank.open(cls, input("Name: "), input("Set 4-digit PIN: "), float(input("Opening deposit: ")))
                print("✅ Account number:", acc.number)
            elif c in "2345" and c:
                acc = bank.accounts[int(input("Account number: "))]
                acc.check_pin(input("PIN: "))
                if c == "2": acc.deposit(float(input("Amount: ")))
                elif c == "3": acc.withdraw(float(input("Amount: ")))
                elif c == "4":
                    dst = bank.accounts[int(input("To account: "))]
                    bank.transfer(acc, dst, float(input("Amount: ")), input("Confirm PIN: "))
                statement(acc)
                bank.save()
            elif c == "0":
                break
        except (BankError, KeyError, ValueError) as e:
            print("❌", type(e).__name__, e)

if __name__ == "__main__":
    path = Path("bank_demo.json" if DEMO else "bank.json")
    bank = Bank(path)
    demo(bank) if DEMO else interactive(bank)
    if DEMO:
        path.unlink(missing_ok=True)

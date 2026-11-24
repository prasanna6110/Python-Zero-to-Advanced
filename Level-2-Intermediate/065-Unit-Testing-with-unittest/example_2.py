# 065 · Unit Testing with unittest — Example 2: setUp and assertRaises
# Run: python example_2.py

import unittest

class Account:
    def __init__(self, balance=0):
        self.balance = balance
    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("insufficient funds")
        self.balance -= amount

class TestAccount(unittest.TestCase):
    def setUp(self):
        self.acc = Account(100)

    def test_withdraw(self):
        self.acc.withdraw(30)
        self.assertEqual(self.acc.balance, 70)

    def test_overdraw(self):
        with self.assertRaises(ValueError):
            self.acc.withdraw(500)

    def test_balance_unchanged_after_error(self):
        with self.assertRaises(ValueError):
            self.acc.withdraw(500)
        self.assertEqual(self.acc.balance, 100)

if __name__ == "__main__":
    unittest.main(verbosity=2)

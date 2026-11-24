# Day 118 · Mocking and Monkey Patching (unittest.mock) — autospec and monkey patching
# Run: python example_3.py

from unittest.mock import create_autospec, patch
import random

class EmailService:
    def send(self, to: str, subject: str, body: str) -> bool: ...

fake = create_autospec(EmailService, instance=True)
fake.send("a@b.com", "Hi", "Hello")
try:
    fake.send("only-one-arg")            # autospec catches calls with the wrong signature
except TypeError as e:
    print("autospec caught:", e)

def roll_dice():
    return random.randint(1, 6)

with patch.object(random, "randint", return_value=6):
    print("rigged dice:", [roll_dice() for _ in range(3)])
print("normal dice is back:", 1 <= roll_dice() <= 6)

class Greeter:
    def hello(self): return "hello"
original = Greeter.hello
Greeter.hello = lambda self: "monkey-patched hello!"
print(Greeter().hello())
Greeter.hello = original
print(Greeter().hello())

# Day 095 · Design Patterns in Python — Factory and Strategy
# Run: python example_1.py

class EmailNotifier:
    def send(self, msg): return f"📧 Email: {msg}"
class SMSNotifier:
    def send(self, msg): return f"📱 SMS: {msg}"
class PushNotifier:
    def send(self, msg): return f"🔔 Push: {msg}"

def notifier_factory(kind):
    return {"email": EmailNotifier, "sms": SMSNotifier, "push": PushNotifier}[kind]()

for kind in ["email", "sms", "push"]:
    print(notifier_factory(kind).send("Your order shipped"))

# Strategy pattern: just pass functions around
strategies = {
    "none": lambda p: p,
    "festive": lambda p: p * 0.8,
    "member": lambda p: p - 100 if p > 500 else p,
}
def checkout(price, strategy):
    return strategies[strategy](price)
print({s: checkout(1000, s) for s in strategies})

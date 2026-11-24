# 085 · Design Patterns in Python — Example 2: Observer (event system)
# Run: python example_2.py

class EventBus:
    def __init__(self):
        self._subs = {}
    def subscribe(self, event, handler):
        self._subs.setdefault(event, []).append(handler)
    def publish(self, event, **data):
        for handler in self._subs.get(event, []):
            handler(**data)

bus = EventBus()
bus.subscribe("order_placed", lambda **d: print(f"  inventory: reserve {d['item']}"))
bus.subscribe("order_placed", lambda **d: print(f"  email: confirm to {d['user']}"))
bus.subscribe("order_placed", lambda **d: print(f"  analytics: +₹{d['amount']}"))
print("Placing order...")
bus.publish("order_placed", item="Laptop", user="asha@mail.com", amount=55000)

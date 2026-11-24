# 085 · Design Patterns in Python

## Common patterns
| Type | Pattern | Idea |
|------|---------|------|
| Creational | **Singleton** | only one instance (in Python, a module-level object is often enough) |
| Creational | **Factory** | create objects without naming their exact class |
| Creational | **Builder** | build complex objects step by step |
| Structural | **Adapter** | make incompatible interfaces work together |
| Structural | **Decorator** | add behaviour dynamically |
| Behavioural | **Strategy** | swap algorithms at runtime |
| Behavioural | **Observer** | notify subscribers of events |
| Behavioural | **Command** | wrap actions as objects (undo/redo) |

## The Pythonic way
Python has first-class functions, duck typing and modules, so many patterns become **much simpler** than in Java or C++. A strategy, for example, can just be a function.

## SOLID principles
**S**ingle responsibility, **O**pen/closed, **L**iskov substitution, **I**nterface segregation, **D**ependency inversion.

## Examples

### Example 1: Factory and Strategy  ([`example_1.py`](example_1.py))

```python
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
```

### Example 2: Observer (event system)  ([`example_2.py`](example_2.py))

```python
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
```

### Example 3: Command with undo, Builder and Adapter  ([`example_3.py`](example_3.py))

```python
class TextEditor:
    def __init__(self): self.text, self.history = "", []
    def execute(self, cmd): cmd.do(self); self.history.append(cmd)
    def undo(self): self.history.pop().undo(self)

class Append:
    def __init__(self, s): self.s = s
    def do(self, ed): ed.text += self.s
    def undo(self, ed): ed.text = ed.text[: -len(self.s)]

ed = TextEditor()
for word in ["Hello", " World", "!!!"]:
    ed.execute(Append(word))
print(ed.text); ed.undo(); print("after undo:", ed.text)

class QueryBuilder:
    def __init__(self, table): self.parts = [f"SELECT * FROM {table}"]
    def where(self, cond): self.parts.append(f"WHERE {cond}"); return self
    def order(self, col): self.parts.append(f"ORDER BY {col}"); return self
    def build(self): return " ".join(self.parts)
print(QueryBuilder("users").where("age > 18").order("name").build())

class OldPrinter:
    def print_text(self, t): return f"[old] {t}"
class PrinterAdapter:                      # adapts the old API to a new .write()
    def __init__(self, old): self.old = old
    def write(self, t): return self.old.print_text(t)
print(PrinterAdapter(OldPrinter()).write("adapted!"))
```

## Practice

1. Build a payment system using Strategy (UPI, Card, Wallet).
2. Add redo to the Command example.
3. Write a weather station using the Observer pattern with 3 displays.

---

[⬅ Level index](../README.md) · [🏠 Course home](../../README.md)

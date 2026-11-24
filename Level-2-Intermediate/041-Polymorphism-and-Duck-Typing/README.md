# 041 · Polymorphism and Duck Typing

## Polymorphism
"Many forms": **one interface, many implementations.** Calling the same method on different objects gives behaviour that suits each object.

## Duck typing
> "If it walks like a duck and quacks like a duck, it's a duck."

Python doesn't care **what type** an object is, only whether it has the **method you need**. That's why `len()` works on strings, lists, dicts and your own classes (if they define `__len__`).

## Kinds of polymorphism in Python
- Method overriding (through inheritance)
- Duck typing (no inheritance needed)
- Operator overloading (`+` works for ints, strings and lists, or your classes through `__add__`)
- `functools.singledispatch` (covered later)

## Examples

### Example 1: Polymorphism through overriding  ([`example_1.py`](example_1.py))

```python
class Shape:
    def area(self):
        raise NotImplementedError

class Rect(Shape):
    def __init__(self, w, h): self.w, self.h = w, h
    def area(self): return self.w * self.h

class Circle(Shape):
    def __init__(self, r): self.r = r
    def area(self): return 3.14159 * self.r ** 2

shapes = [Rect(3, 4), Circle(2), Rect(1, 1)]
for s in shapes:
    print(f"{type(s).__name__}: {s.area():.2f}")
print("Total:", round(sum(s.area() for s in shapes), 2))
```

### Example 2: Duck typing  ([`example_2.py`](example_2.py))

```python
class Duck:
    def speak(self): return "Quack"

class Robot:
    def speak(self): return "Beep boop"

class Person:
    def speak(self): return "Hello"

def make_it_speak(thing):       # no type checks at all
    print(thing.speak())

for obj in [Duck(), Robot(), Person()]:
    make_it_speak(obj)
```

### Example 3: Built-in polymorphism  ([`example_3.py`](example_3.py))

```python
print(len("hello"), len([1, 2, 3]), len({"a": 1}))
print(1 + 2, "a" + "b", [1] + [2])

class Playlist:
    def __init__(self, songs): self.songs = songs
    def __len__(self): return len(self.songs)
    def __iter__(self): return iter(self.songs)

pl = Playlist(["song1", "song2", "song3"])
print(len(pl), list(pl), "song2" in pl)
```

## Practice

1. Create `PDFExporter` and `CSVExporter` classes, each with `export(data)`, and call them through the same loop.
2. Make your own class work with `len()` and a `for` loop.
3. What is the difference between polymorphism with inheritance and duck typing?

---

[⬅ Level index](../README.md) · [🏠 Course home](../../README.md)

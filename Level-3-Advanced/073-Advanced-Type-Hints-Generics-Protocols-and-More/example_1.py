# 073 · Advanced Type Hints: Generics, Protocols and More — Example 1: Generic functions and classes (3.12 syntax)
# Run: python example_1.py

def first[T](items: list[T]) -> T:
    return items[0]

class Stack[T]:
    def __init__(self) -> None:
        self._items: list[T] = []
    def push(self, item: T) -> None:
        self._items.append(item)
    def pop(self) -> T:
        return self._items.pop()

type Pair[T] = tuple[T, T]

def swap[T](p: Pair[T]) -> Pair[T]:
    return p[1], p[0]

s: Stack[int] = Stack()
s.push(1); s.push(2)
print(first(["a", "b"]), s.pop(), swap((1, 2)))

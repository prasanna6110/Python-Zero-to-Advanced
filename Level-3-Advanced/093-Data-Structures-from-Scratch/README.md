# 093 · Data Structures from Scratch

## Why build them yourself?
Building them by hand teaches you how they work, what they cost and how to answer interview questions. In real code, use the built-ins (`list`, `dict`, `deque`, `heapq`).

| Structure | Key operations | Built-in equivalent |
|-----------|----------------|---------------------|
| Stack (LIFO) | push and pop O(1) | `list` |
| Queue (FIFO) | enqueue and dequeue O(1) | `collections.deque` |
| Linked list | insert at head O(1), search O(n) | — |
| Binary search tree | search, insert O(log n) on average | `sortedcontainers` (PyPI) |
| Hash table | get and set O(1) on average | `dict` |
| Graph | adjacency list | `dict[node, list]` |
| Trie | prefix search O(length of word) | — |

## Big-O cheat sheet
O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ)

## Examples

### Example 1: Linked list  ([`example_1.py`](example_1.py))

```python
class Node:
    def __init__(self, value, next=None):
        self.value, self.next = value, next

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    def push_front(self, v):
        self.head = Node(v, self.head); self.size += 1
    def append(self, v):
        node = Node(v)
        if not self.head:
            self.head = node
        else:
            cur = self.head
            while cur.next: cur = cur.next
            cur.next = node
        self.size += 1
    def reverse(self):
        prev, cur = None, self.head
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        self.head = prev
    def __iter__(self):
        cur = self.head
        while cur:
            yield cur.value
            cur = cur.next
    def __repr__(self):
        return " -> ".join(map(str, self)) + " -> None"

ll = LinkedList()
for v in [2, 3, 4]: ll.append(v)
ll.push_front(1)
print(ll, "size", ll.size)
ll.reverse()
print(ll)
```

### Example 2: Binary search tree  ([`example_2.py`](example_2.py))

```python
class BST:
    class _Node:
        def __init__(self, key):
            self.key, self.left, self.right = key, None, None

    def __init__(self):
        self.root = None

    def insert(self, key):
        def _ins(node, key):
            if node is None: return BST._Node(key)
            if key < node.key: node.left = _ins(node.left, key)
            elif key > node.key: node.right = _ins(node.right, key)
            return node
        self.root = _ins(self.root, key)

    def __contains__(self, key):
        node = self.root
        while node:
            if key == node.key: return True
            node = node.left if key < node.key else node.right
        return False

    def inorder(self, node="start"):
        node = self.root if node == "start" else node
        if node:
            yield from self.inorder(node.left)
            yield node.key
            yield from self.inorder(node.right)

    def height(self, node="start"):
        node = self.root if node == "start" else node
        return 0 if node is None else 1 + max(self.height(node.left), self.height(node.right))

t = BST()
for k in [50, 30, 70, 20, 40, 60, 80, 35]:
    t.insert(k)
print("sorted:", list(t.inorder()), "| height:", t.height())
print(40 in t, 45 in t)
```

### Example 3: Trie and a hash table  ([`example_3.py`](example_3.py))

```python
class Trie:
    def __init__(self): self.root = {}
    def insert(self, word):
        node = self.root
        for ch in word: node = node.setdefault(ch, {})
        node["$"] = True
    def starts_with(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node: return []
            node = node[ch]
        out = []
        def walk(n, path):
            if "$" in n: out.append(prefix + path)
            for ch, child in n.items():
                if ch != "$": walk(child, path + ch)
        walk(node, "")
        return sorted(out)

trie = Trie()
for w in ["python", "pycharm", "pytest", "java", "pandas"]:
    trie.insert(w)
print("autocomplete 'py':", trie.starts_with("py"))

class HashTable:
    def __init__(self, size=8): self.buckets = [[] for _ in range(size)]
    def _bucket(self, key): return self.buckets[hash(key) % len(self.buckets)]
    def set(self, key, value):
        b = self._bucket(key)
        for i, (k, _) in enumerate(b):
            if k == key: b[i] = (key, value); return
        b.append((key, value))
    def get(self, key):
        for k, v in self._bucket(key):
            if k == key: return v
        raise KeyError(key)

ht = HashTable()
ht.set("apple", 5); ht.set("mango", 9); ht.set("apple", 7)
print(ht.get("apple"), ht.get("mango"))
```

## Practice

1. Build a stack that also returns its minimum in O(1).
2. Add a `delete` method to the BST.
3. Implement a queue using two stacks.

---

[⬅ Level index](../README.md) · [🏠 Course home](../../README.md)

# Day 106 · Data Structures from Scratch — Linked list
# Run: python example_1.py

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

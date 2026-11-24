# 093 · Data Structures from Scratch — Example 2: Binary search tree
# Run: python example_2.py

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

# Day 106 · Data Structures from Scratch — Trie and a hash table
# Run: python example_3.py

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

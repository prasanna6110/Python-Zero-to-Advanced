# 041 · Polymorphism and Duck Typing — Example 3: Built-in polymorphism
# Run: python example_3.py

print(len("hello"), len([1, 2, 3]), len({"a": 1}))
print(1 + 2, "a" + "b", [1] + [2])

class Playlist:
    def __init__(self, songs): self.songs = songs
    def __len__(self): return len(self.songs)
    def __iter__(self): return iter(self.songs)

pl = Playlist(["song1", "song2", "song3"])
print(len(pl), list(pl), "song2" in pl)

# Day 042 · Constructors, Instance and Class Attributes — The shared mutable class attribute bug
# Run: python example_3.py

class BadTeam:
    members = []             # shared by ALL teams!
    def add(self, name):
        self.members.append(name)

class GoodTeam:
    def __init__(self):
        self.members = []    # each team gets its own list
    def add(self, name):
        self.members.append(name)

t1, t2 = BadTeam(), BadTeam()
t1.add("Asha")
print("BadTeam t2:", t2.members)
g1, g2 = GoodTeam(), GoodTeam()
g1.add("Asha")
print("GoodTeam g2:", g2.members)

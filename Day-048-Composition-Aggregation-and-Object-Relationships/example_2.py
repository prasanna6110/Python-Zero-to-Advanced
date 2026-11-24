# Day 048 · Composition, Aggregation and Object Relationships — Aggregation: a team uses players that exist independently
# Run: python example_2.py

class Player:
    def __init__(self, name, role):
        self.name, self.role = name, role
    def __repr__(self):
        return f"{self.name}({self.role})"

class Team:
    def __init__(self, name):
        self.name, self.players = name, []
    def add(self, player):
        self.players.append(player)
    def remove(self, player):
        self.players.remove(player)

virat = Player("Virat", "batter")
bumrah = Player("Bumrah", "bowler")
india = Team("India")
india.add(virat); india.add(bumrah)
rcb = Team("RCB")
rcb.add(virat)                           # the same player belongs to two teams
india.remove(virat)
print(india.players, rcb.players, "| player still exists:", virat)

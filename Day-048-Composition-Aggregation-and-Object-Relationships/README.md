# Day 048 · Composition, Aggregation and Object Relationships

_Intermediate_

## Relationships between objects
| Relationship | Meaning | Example |
|--------------|---------|---------|
| **Inheritance** ("is-a") | a child *is a* kind of the parent | `Dog` is an `Animal` |
| **Composition** ("has-a", strong) | an object **owns** its parts; they live and die together | a `Car` has an `Engine` |
| **Aggregation** ("has-a", weak) | an object **uses** parts that exist on their own | a `Team` has `Player`s |
| **Association** | objects simply work together | a `Teacher` teaches a `Student` |

## "Favour composition over inheritance"
Deep inheritance trees are fragile. Composition lets you **swap parts** (give a robot a different battery) and keeps classes small and focused.

**Rule of thumb:** use inheritance only when the "is-a" relationship is genuinely true and you want polymorphism. Otherwise, use composition.

## Examples

### Example 1: Composition: a car owns its engine  ([`example_1.py`](example_1.py))

```python
class Engine:
    def __init__(self, hp):
        self.hp = hp
        self.running = False
    def start(self):
        self.running = True
        return f"{self.hp}hp engine started"

class Wheels:
    def __init__(self, count=4):
        self.count = count

class Car:
    def __init__(self, model, hp):
        self.model = model
        self.engine = Engine(hp)        # created and owned by the Car
        self.wheels = Wheels()

    def drive(self):
        return f"{self.model}: {self.engine.start()}, rolling on {self.wheels.count} wheels"

print(Car("Nexon EV", 143).drive())
```

### Example 2: Aggregation: a team uses players that exist independently  ([`example_2.py`](example_2.py))

```python
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
```

### Example 3: Swappable parts: composition instead of inheritance  ([`example_3.py`](example_3.py))

```python
class LoudSpeaker:
    def say(self, text): return text.upper() + "!!!"

class Whisper:
    def say(self, text): return text.lower() + "..."

class Robot:
    def __init__(self, name, voice):
        self.name, self.voice = name, voice
    def greet(self):
        return f"{self.name}: {self.voice.say('Hello Human')}"

r = Robot("R2", LoudSpeaker())
print(r.greet())
r.voice = Whisper()                      # change behaviour at runtime
print(r.greet())
```

## Practice

1. Build `Computer` that is composed of `CPU`, `RAM` and `Storage`.
2. Model `Department` and `Professor` with aggregation.
3. Rewrite a 3-level inheritance example using composition.

---

[⬅ Day 047](../Day-047-Polymorphism-and-Duck-Typing/README.md) · [🏠 Home](../README.md) · [Day 049 ➡](../Day-049-Abstract-Classes-and-Interfaces-abc/README.md)

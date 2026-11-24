# Day 048 · Composition, Aggregation and Object Relationships — Composition: a car owns its engine
# Run: python example_1.py

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

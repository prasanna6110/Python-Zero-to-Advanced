# 038 · Inheritance — Example 2: Multilevel inheritance
# Run: python example_2.py

class Vehicle:
    def start(self):
        return "Engine started"

class Car(Vehicle):
    wheels = 4
    def drive(self):
        return "Driving"

class ElectricCar(Car):
    def start(self):
        return "Silent start ⚡ (" + super().start() + ")"

tesla = ElectricCar()
print(tesla.start(), tesla.drive(), tesla.wheels)
print(ElectricCar.__mro__)

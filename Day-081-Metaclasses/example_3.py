# Day 081 · Metaclasses — __call__ for singletons and __prepare__ for ordering
# Run: python example_3.py

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=Singleton):
    def __init__(self):
        print("  connecting once...")

print(Database() is Database())

class Recorder(type):
    @classmethod
    def __prepare__(mcls, name, bases):
        print(f"  preparing namespace for {name}")
        return {"created_by": "Recorder"}
    def __new__(mcls, name, bases, ns):
        ns["fields"] = [k for k in ns if not k.startswith("__") and k != "created_by"]
        return super().__new__(mcls, name, bases, ns)

class Form(metaclass=Recorder):
    username = str
    password = str

print(Form.fields, Form.created_by)

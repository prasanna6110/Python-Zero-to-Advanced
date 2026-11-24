# Day 013 · match-case (Structural Pattern Matching) — Matching sequences and dicts
# Run: python example_3.py

def handle(command):
    match command.split():
        case ["go", direction]:
            return f"Going {direction}"
        case ["pick", "up", item]:
            return f"Picked up {item}"
        case ["quit" | "exit"]:
            return "Bye!"
        case [first, *rest]:
            return f"Unknown command {first!r} with args {rest}"

for cmd in ["go north", "pick up sword", "exit", "dance fast now"]:
    print(handle(cmd))

event = {"type": "click", "x": 10, "y": 20}
match event:
    case {"type": "click", "x": x, "y": y}:
        print(f"Clicked at ({x}, {y})")
    case {"type": "key", "key": k}:
        print("Key pressed:", k)

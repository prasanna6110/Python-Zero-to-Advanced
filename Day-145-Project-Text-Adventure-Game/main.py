# Day 145 · Project: Text Adventure Game — Escape the Lab: Text Adventure
# Run: python main.py

import sys

DEMO = not sys.stdin.isatty()
DEMO_COMMANDS = iter(["look", "go east", "take torch", "go west", "go north", "take key", "inventory",
                      "go south", "go south", "use key", "go south"])

WORLD = {
    "Lab": {"desc": "You're in the power systems lab. Oscilloscopes hum quietly.",
            "exits": {"north": "Library", "east": "Store Room", "south": "Corridor"}, "items": []},
    "Store Room": {"desc": "Dusty shelves full of old transformers.", "exits": {"west": "Lab"}, "items": ["torch"]},
    "Library": {"desc": "Silent shelves. Something shines under a desk...", "exits": {"south": "Lab"},
                "items": ["key"], "dark": True},
    "Corridor": {"desc": "A long corridor. The main gate to the south is LOCKED.", "exits": {"north": "Lab"},
                 "items": [], "locked": "south"},
    "Exit": {"desc": "Fresh air! You escaped the lab. 🎉", "exits": {}, "items": []},
}

def get_command():
    if DEMO:
        try:
            cmd = next(DEMO_COMMANDS)
        except StopIteration:
            return "quit"
        print("> " + cmd); return cmd
    return input("> ").strip().lower()

def main():
    room, inventory = "Lab", []
    print("🏫 ESCAPE THE LAB. Type commands like 'go north', 'take torch', 'use key'.\n")
    print(WORLD[room]["desc"])
    while room != "Exit":
        match get_command().split():
            case ["look"]:
                r = WORLD[room]
                if r.get("dark") and "torch" not in inventory:
                    print("It's too dark to see anything. You need light.")
                else:
                    print(r["desc"], "| Items:", r["items"] or "none", "| Exits:", ", ".join(r["exits"]))
            case ["go", direction]:
                exits = WORLD[room]["exits"]
                if WORLD[room].get("locked") == direction:
                    print("🔒 The gate is locked.")
                elif direction in exits:
                    room = exits[direction]
                    print(f"You walk {direction} to the {room}. {WORLD[room]['desc']}")
                else:
                    print("You can't go that way.")
            case ["take", item]:
                r = WORLD[room]
                if r.get("dark") and "torch" not in inventory:
                    print("You fumble in the dark and find nothing.")
                elif item in r["items"]:
                    r["items"].remove(item); inventory.append(item); print(f"Taken: {item}")
                else:
                    print(f"No {item} here.")
            case ["use", "key"] if "key" in inventory and room == "Corridor":
                WORLD["Corridor"]["locked"] = None
                WORLD["Corridor"]["exits"]["south"] = "Exit"
                print("🔓 The gate unlocks with a loud click!")
            case ["inventory" | "i"]:
                print("You carry:", inventory or "nothing")
            case ["quit"]:
                print("Game over."); return
            case _:
                print("I don't understand that.")
    print("🏆 YOU WIN!")

if __name__ == "__main__":
    main()

# Day 130 · Project: Rock Paper Scissors — Rock Paper Scissors (Lizard Spock)
# Run: python main.py

import random
import sys

DEMO = not sys.stdin.isatty()
DEMO_MOVES = iter(["rock", "paper", "spock", "lizard", "scissors"])

BEATS = {
    "rock": {"scissors": "crushes", "lizard": "crushes"},
    "paper": {"rock": "covers", "spock": "disproves"},
    "scissors": {"paper": "cuts", "lizard": "decapitates"},
    "lizard": {"spock": "poisons", "paper": "eats"},
    "spock": {"scissors": "smashes", "rock": "vaporizes"},
}

def get_move():
    if DEMO:
        move = next(DEMO_MOVES)
        print(f"Your move: {move}")
        return move
    while True:
        move = input(f"Your move {list(BEATS)} or 'q': ").strip().lower()
        if move in BEATS or move == "q":
            return move
        print("Invalid move!")

def main(rounds=5):
    score = {"you": 0, "computer": 0, "draw": 0}
    print(f"🪨📄✂️🦎🖖  Best of {rounds}")
    for r in range(1, rounds + 1):
        print(f"\n--- Round {r} ---")
        you = get_move()
        if you == "q":
            break
        cpu = random.choice(list(BEATS))
        print(f"Computer: {cpu}")
        if you == cpu:
            print("🤝 Draw"); score["draw"] += 1
        elif cpu in BEATS[you]:
            print(f"✅ {you} {BEATS[you][cpu]} {cpu}"); score["you"] += 1
        else:
            print(f"❌ {cpu} {BEATS[cpu][you]} {you}"); score["computer"] += 1
    print("\nFinal score:", score)
    print("🏆 You win!" if score["you"] > score["computer"] else
          "🤖 Computer wins!" if score["computer"] > score["you"] else "It's a tie!")

if __name__ == "__main__":
    if DEMO:
        random.seed(3)
    main()

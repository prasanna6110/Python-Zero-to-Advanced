# Day 129 · Project: Number Guessing Game — Number Guessing Game
# Run: python main.py

import random
import sys

DEMO = not sys.stdin.isatty()          # play automatically when not run in a terminal

def ask(prompt):
    if DEMO:
        return None
    return input(prompt)

LEVELS = {"1": ("Easy", 50, 10), "2": ("Medium", 100, 7), "3": ("Hard", 500, 9)}

def play():
    print("🎯 NUMBER GUESSING GAME")
    for k, (name, top, tries) in LEVELS.items():
        print(f"  {k}. {name}: 1-{top}, {tries} attempts")
    choice = ask("Choose level (1/2/3): ") if not DEMO else "2"
    name, top, max_tries = LEVELS.get(choice, LEVELS["1"])
    secret = random.randint(1, top)
    low, high = 1, top
    for attempt in range(1, max_tries + 1):
        if DEMO:
            guess = (low + high) // 2           # the demo player uses binary search
            print(f"Attempt {attempt}: guess -> {guess}")
        else:
            raw = ask(f"Attempt {attempt}/{max_tries} - your guess: ")
            if not raw.strip().isdigit():
                print("Please enter a whole number.")
                continue
            guess = int(raw)
        if guess < secret:
            print("  📉 Too low!"); low = guess + 1
        elif guess > secret:
            print("  📈 Too high!"); high = guess - 1
        else:
            score = (max_tries - attempt + 1) * 10
            print(f"🎉 Correct! The number was {secret}. Score: {score}")
            return score
    print(f"😢 Out of attempts. The number was {secret}.")
    return 0

if __name__ == "__main__":
    if DEMO:
        random.seed(7)
    play()

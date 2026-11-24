# Day 015 · while Loops — Guessing game (simulated guesses)
# Run: python example_3.py

secret = 42
guesses = iter([10, 60, 40, 42])   # stands in for input() so the example runs on its own
attempts = 0
while True:
    guess = next(guesses)
    attempts += 1
    if guess < secret:
        print(guess, "-> too low")
    elif guess > secret:
        print(guess, "-> too high")
    else:
        print(guess, f"-> correct in {attempts} attempts!")
        break

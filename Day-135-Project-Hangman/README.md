# Day 135 · Project: Hangman

_Projects_

**Concepts:** strings, sets, loops, ASCII art lists, categories of words.

Guess the hidden word one letter at a time before the hangman drawing is finished.

## Code

### Hangman  ([`main.py`](main.py))

```python
import random
import sys

DEMO = not sys.stdin.isatty()
WORDS = {
    "programming": ["python", "variable", "function", "decorator", "generator", "iterator"],
    "electrical": ["transformer", "inverter", "microgrid", "capacitor", "resistance"],
}
STAGES = [
    "  +---+\n      |\n      |\n      |\n     ===",
    "  +---+\n  O   |\n      |\n      |\n     ===",
    "  +---+\n  O   |\n  |   |\n      |\n     ===",
    "  +---+\n  O   |\n /|   |\n      |\n     ===",
    "  +---+\n  O   |\n /|\\  |\n      |\n     ===",
    "  +---+\n  O   |\n /|\\  |\n /    |\n     ===",
    "  +---+\n  O   |\n /|\\  |\n / \\  |\n     ===",
]

def play():
    category = random.choice(list(WORDS))
    word = random.choice(WORDS[category])
    guessed, wrong = set(), 0
    demo_letters = iter("etaoinsrhldcumfpgwybvkxjqz")
    print(f"🪢 HANGMAN | category: {category} | {len(word)} letters")
    while wrong < len(STAGES) - 1:
        print(STAGES[wrong])
        print("Word:", " ".join(c if c in guessed else "_" for c in word))
        if all(c in guessed for c in word):
            print(f"🎉 You won! The word was '{word}'")
            return True
        if DEMO:
            letter = next(demo_letters)
            print("Guess a letter:", letter)
        else:
            letter = input("Guess a letter: ").strip().lower()
            if len(letter) != 1 or not letter.isalpha():
                print("Enter one letter."); continue
        if letter in guessed:
            print("Already guessed!"); continue
        guessed.add(letter)
        if letter not in word:
            wrong += 1
            print(f"❌ '{letter}' is not in the word ({len(STAGES) - 1 - wrong} lives left)")
    print(STAGES[-1])
    print(f"💀 You lost! The word was '{word}'")
    return False

if __name__ == "__main__":
    if DEMO:
        random.seed(4)
    play()
```

## Extend this project

1. Load the words from a text file.
2. Add a hint that reveals one letter but costs a life.
3. Add a multiplayer mode where one player types the secret word.

---

[⬅ Day 134](../Day-134-Project-Dice-Rolling-Simulator-and-Probability-Lab/README.md) · [🏠 Home](../README.md) · [Day 136 ➡](../Day-136-Project-Tic-Tac-Toe-with-an-Unbeatable-AI/README.md)

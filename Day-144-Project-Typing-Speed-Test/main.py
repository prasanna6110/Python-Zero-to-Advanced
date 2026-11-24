# Day 144 · Project: Typing Speed Test — Typing Speed Test
# Run: python main.py

import difflib
import random
import sys
import time

DEMO = not sys.stdin.isatty()
SENTENCES = [
    "Python makes programming simple and fun for everyone.",
    "Practice every day and you will master any skill.",
    "A microgrid can operate connected to the grid or in island mode.",
    "Readability counts and simple is better than complex.",
]

def measure(target, typed, seconds):
    words = len(typed.split())
    wpm = words / (seconds / 60) if seconds else 0
    accuracy = difflib.SequenceMatcher(None, target, typed).ratio() * 100
    mistakes = [(t, y) for t, y in zip(target.split(), typed.split()) if t != y]
    return wpm, accuracy, mistakes

def main():
    target = random.choice(SENTENCES)
    print("⌨️ TYPING SPEED TEST\nType this sentence:\n")
    print("   " + target + "\n")
    if DEMO:
        typed = target.replace("every", "evry").replace("simple", "simpel")
        seconds = 9.5
        print("(demo) typed:", typed)
    else:
        input("Press Enter when ready...")
        start = time.perf_counter()
        typed = input("> ")
        seconds = time.perf_counter() - start
    wpm, acc, mistakes = measure(target, typed, seconds)
    print(f"\n⏱ Time: {seconds:.1f}s | 🚀 Speed: {wpm:.0f} WPM | 🎯 Accuracy: {acc:.1f}%")
    for expected, got in mistakes:
        print(f"   ✗ typed {got!r}, expected {expected!r}")
    rank = "Pro 🏆" if wpm > 60 and acc > 95 else "Good 👍" if wpm > 35 else "Keep practising 💪"
    print("Level:", rank)

if __name__ == "__main__":
    if DEMO:
        random.seed(2)
    main()

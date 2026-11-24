# Day 144 · Project: Typing Speed Test

_Projects_

**Concepts:** `time.perf_counter`, string comparison, `difflib`, WPM and accuracy calculations.

Type a sentence as fast as you can, and see your **words per minute**, your accuracy and exactly which words you got wrong.

## Code

### Typing Speed Test  ([`main.py`](main.py))

```python
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
```

## Extend this project

1. Run 5 rounds and show your average and best scores.
2. Save the results to CSV and plot your progress.
3. Build a Tkinter version that shows correct and incorrect letters in colour as you type.

---

[⬅ Day 143](../Day-143-Project-Shopping-Bill-Generator-with-GST/README.md) · [🏠 Home](../README.md) · [Day 145 ➡](../Day-145-Project-Text-Adventure-Game/README.md)

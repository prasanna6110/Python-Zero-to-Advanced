# Day 140 · Project: Text Analyzer

_Projects_

**Concepts:** string methods, regex, `Counter`, reading files, statistics, readability formulas.

Paste text, or give it a file, and get word, sentence and character counts, the most common words (with stop words removed), reading time and a **Flesch readability** score.

## Code

### Text Analyzer  ([`main.py`](main.py))

```python
import re
import sys
from collections import Counter

DEMO = not sys.stdin.isatty()
SAMPLE = """Python is a high-level programming language. It was designed to be readable and simple.
Python supports many programming paradigms, including object-oriented and functional programming.
Today Python is used in web development, data science, machine learning, automation and electrical
engineering simulations. Learning Python day by day is the best way to master it!"""
STOP = set("a an the is it to and or of in on for be was were are with by as at this that from".split())

def syllables(word):
    word = word.lower()
    groups = re.findall(r"[aeiouy]+", word)
    count = len(groups) - (1 if word.endswith("e") and len(groups) > 1 else 0)
    return max(1, count)

def analyze(text):
    words = re.findall(r"[A-Za-z']+", text)
    sentences = [s for s in re.split(r"[.!?]+", text) if s.strip()]
    syl = sum(syllables(w) for w in words)
    flesch = 206.835 - 1.015 * (len(words) / len(sentences)) - 84.6 * (syl / len(words))
    freq = Counter(w.lower() for w in words if w.lower() not in STOP)
    return {
        "characters": len(text), "characters (no spaces)": len(text.replace(" ", "").replace("\n", "")),
        "words": len(words), "unique words": len({w.lower() for w in words}),
        "sentences": len(sentences), "paragraphs": text.count("\n\n") + 1,
        "avg word length": round(sum(map(len, words)) / len(words), 2),
        "avg sentence length": round(len(words) / len(sentences), 1),
        "reading time (min)": round(len(words) / 200, 2),
        "flesch score": round(flesch, 1),
        "longest word": max(words, key=len),
        "top words": freq.most_common(5),
    }

def level(score):
    return ("very easy" if score > 80 else "easy" if score > 60 else
            "standard" if score > 50 else "difficult" if score > 30 else "very difficult")

if __name__ == "__main__":
    if DEMO:
        text = SAMPLE
    elif len(sys.argv) > 1:
        text = open(sys.argv[1], encoding="utf-8").read()
    else:
        print("Paste text, then press Enter on an empty line:")
        lines = iter(input, "")
        text = "\n".join(lines)
    stats = analyze(text)
    print("📊 TEXT ANALYSIS")
    for k, v in stats.items():
        print(f"  {k:<24} {v}")
    print(f"  readability             {level(stats['flesch score'])}")
```

## Extend this project

1. Detect the language of the text (English or Hinglish) using word lists.
2. Find the repeated phrases (bigrams and trigrams).
3. Make a word cloud with the `wordcloud` library.

---

[⬅ Day 139](../Day-139-Project-Student-Report-Card-System/README.md) · [🏠 Home](../README.md) · [Day 141 ➡](../Day-141-Project-Caesar-and-Vigenere-Cipher-Tool/README.md)

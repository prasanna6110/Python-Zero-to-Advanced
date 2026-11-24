# Day 172 · Project: Spam Classifier with Naive Bayes (ML from Scratch) — Naive Bayes Spam Classifier
# Run: python main.py

import math
import random
import re
from collections import Counter

SPAM = ["win a free iphone now click here", "congratulations you won a lottery claim prize now",
        "free money offer limited time click link", "earn cash fast work from home guaranteed",
        "claim your free gift card today", "urgent your account will be closed verify now click",
        "cheap loans approved instantly no documents", "you are selected winner claim reward now",
        "exclusive deal buy now get 90 percent off", "free recharge offer click to activate",
        "lowest price medicines order now free delivery", "double your money in 7 days invest now"]
HAM = ["are we meeting for the micro grids lab tomorrow", "please send the python assignment notes",
       "mom called about dinner tonight", "the project review is scheduled on friday",
       "can you share the github repo link", "happy birthday hope you have a great day",
       "the professor uploaded the mid term syllabus", "lets go to the library after class",
       "your parcel has been delivered at the hostel gate", "meeting notes for the research paper attached",
       "did you finish day 50 of the python course", "reminder the exam starts at 10 am"]

def tokenize(text):
    return re.findall(r"[a-z]+", text.lower())

class NaiveBayes:
    def fit(self, texts, labels):
        self.classes = set(labels)
        self.priors = {c: labels.count(c) / len(labels) for c in self.classes}
        self.counts = {c: Counter() for c in self.classes}
        for t, c in zip(texts, labels):
            self.counts[c].update(tokenize(t))
        self.vocab = set().union(*self.counts.values())
        self.totals = {c: sum(self.counts[c].values()) for c in self.classes}
        return self

    def log_prob(self, text, c):
        lp = math.log(self.priors[c])
        for w in tokenize(text):
            lp += math.log((self.counts[c][w] + 1) / (self.totals[c] + len(self.vocab)))   # Laplace smoothing
        return lp

    def predict(self, text):
        scores = {c: self.log_prob(text, c) for c in self.classes}
        best = max(scores, key=scores.get)
        m = max(scores.values())
        prob = math.exp(scores[best] - m) / sum(math.exp(s - m) for s in scores.values())
        return best, prob

    def top_words(self, c, n=6):
        other = [k for k in self.classes if k != c][0]
        ratio = {w: (self.counts[c][w] + 1) / (self.counts[other][w] + 1) for w in self.vocab}
        return sorted(ratio, key=ratio.get, reverse=True)[:n]

def evaluate(model, texts, labels):
    tp = fp = tn = fn = 0
    for t, y in zip(texts, labels):
        p, _ = model.predict(t)
        tp += p == y == "spam"; tn += p == y == "ham"
        fp += p == "spam" != y; fn += p == "ham" != y
    print(f"Confusion matrix: TP={tp} FP={fp} TN={tn} FN={fn}")
    print(f"Accuracy {(tp + tn) / len(labels):.0%} | Precision {tp / max(tp + fp, 1):.0%} | Recall {tp / max(tp + fn, 1):.0%}")

if __name__ == "__main__":
    random.seed(0)
    data = [(t, "spam") for t in SPAM] + [(t, "ham") for t in HAM]
    random.shuffle(data)
    split = int(len(data) * 0.7)
    train, test = data[:split], data[split:]
    model = NaiveBayes().fit([t for t, _ in train], [l for _, l in train])
    print(f"Trained on {len(train)} messages, vocabulary of {len(model.vocab)} words")
    evaluate(model, [t for t, _ in test], [l for _, l in test])
    print("Most 'spammy' words:", model.top_words("spam"))
    for msg in ["claim your free prize now", "can we discuss the python project tomorrow",
                "limited offer win cash", "notes for the exam"]:
        label, p = model.predict(msg)
        print(f"  {'🚫' if label == 'spam' else '✅'} {label:<4} ({p:.0%})  {msg}")

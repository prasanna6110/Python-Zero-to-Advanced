# Day 169 · Project: Mini Search Engine (Inverted Index + TF-IDF) — Mini Search Engine
# Run: python main.py

import math
import re
import sys
from collections import Counter, defaultdict

DEMO = not sys.stdin.isatty()
DOCS = {
    "day-001": "Introduction to Python: install Python, write your first print program and use the REPL.",
    "day-047": "Generators use yield to produce values lazily. Generators save memory for big data pipelines.",
    "day-076": "Asyncio runs many coroutines on one thread. Use await and the event loop for network IO.",
    "day-074": "Threading runs threads in one process. The GIL limits CPU bound threads but IO bound work speeds up.",
    "day-075": "Multiprocessing uses processes for CPU bound work and true parallelism without the GIL.",
    "day-088": "SQLite databases with sqlite3: tables, SQL queries, joins and transactions in Python.",
    "day-140": "Project: text analyzer counts words, sentences and readability of any text file.",
}
STOP = set("a an the and or of to in on for is are by with use your any many into one".split())

def tokenize(text):
    return [w for w in re.findall(r"[a-z0-9]+", text.lower()) if w not in STOP]

class SearchEngine:
    def __init__(self, docs):
        self.docs = docs
        self.index = defaultdict(dict)              # word -> {doc: count}
        self.lengths = {}
        for doc_id, text in docs.items():
            tokens = tokenize(text)
            self.lengths[doc_id] = len(tokens)
            for word, n in Counter(tokens).items():
                self.index[word][doc_id] = n

    def idf(self, word):
        return math.log(len(self.docs) / (1 + len(self.index.get(word, {})))) + 1

    def search(self, query, top=3):
        scores = Counter()
        for word in tokenize(query):
            for doc, n in self.index.get(word, {}).items():
                scores[doc] += (n / self.lengths[doc]) * self.idf(word)
        return scores.most_common(top)

    def snippet(self, doc, query):
        words = set(tokenize(query))
        text = self.docs[doc]
        return re.sub(r"\b(\w+)\b", lambda m: f"**{m.group(1)}**" if m.group(1).lower() in words else m.group(1), text)

    def suggest(self, word):
        import difflib
        return difflib.get_close_matches(word, self.index.keys(), n=1)

if __name__ == "__main__":
    engine = SearchEngine(DOCS)
    print(f"🔎 Indexed {len(DOCS)} documents, {len(engine.index)} unique words")
    queries = ["GIL cpu bound", "generators memory", "database sql", "asynco network"] if DEMO else []
    while True:
        q = queries.pop(0) if DEMO and queries else (None if DEMO else input("\nSearch (empty to quit): "))
        if not q:
            break
        print(f"\nQuery: {q!r}")
        results = engine.search(q)
        if not results:
            fixes = [s for w in tokenize(q) for s in engine.suggest(w)]
            print("  No results.", f"Did you mean: {' '.join(fixes)}?" if fixes else "")
            if fixes:
                results = engine.search(" ".join(fixes))
        for doc, score in results:
            print(f"  {score:.3f}  {doc}: {engine.snippet(doc, q)[:95]}")

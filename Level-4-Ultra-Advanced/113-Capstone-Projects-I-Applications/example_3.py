# 113 · Capstone Projects I: Applications — Example 3: Quiz Engine (JSON data + closures + strategies)
# Run: python example_3.py

import json, random
from typing import Callable

QUESTIONS_JSON = """[
 {"q": "Output of len({1, 1, 2})?", "options": ["1", "2", "3"], "answer": "2", "level": 1},
 {"q": "Which keyword makes a generator?", "options": ["return", "yield", "async"], "answer": "yield", "level": 1},
 {"q": "Default metaclass of every class?", "options": ["object", "type", "ABCMeta"], "answer": "type", "level": 3},
 {"q": "What does the GIL limit?", "options": ["I/O", "Parallel bytecode execution", "Memory"], "answer": "Parallel bytecode execution", "level": 3},
 {"q": "Which module do asyncio's selectors build on?", "options": ["selectors", "socketserver", "ssl"], "answer": "selectors", "level": 4}
]"""

def make_scorer(strategy: str) -> Callable[[dict, bool], int]:
    streak = 0
    def flat(q, correct): return 1 if correct else 0
    def weighted(q, correct): return q["level"] if correct else 0
    def streak_bonus(q, correct):
        nonlocal streak
        streak = streak + 1 if correct else 0
        return streak if correct else 0
    return {"flat": flat, "weighted": weighted, "streak": streak_bonus}[strategy]

def run_quiz(questions, answer_fn, strategy="weighted"):
    score_fn, score = make_scorer(strategy), 0
    for i, q in enumerate(questions, 1):
        opts = q["options"][:]
        random.shuffle(opts)
        choice = answer_fn(q, opts)
        correct = choice == q["answer"]
        score += score_fn(q, correct)
        print(f"Q{i}. {q['q']}\n    options: {opts}\n    you: {choice} -> {'✅' if correct else '❌ ' + q['answer']}")
    return score

random.seed(5)
questions = json.loads(QUESTIONS_JSON)
smart_player = lambda q, opts: q["answer"] if q["level"] < 4 else opts[0]   # simulates the user's answers
for strategy in ["flat", "weighted", "streak"]:
    print(f"\n=== strategy: {strategy} ===")
    print("FINAL SCORE:", run_quiz(questions, smart_player, strategy))

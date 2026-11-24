# 061 · collections Module — Example 2: deque as a queue and a sliding window
# Run: python example_2.py

from collections import deque

q = deque(["t1", "t2"])
q.append("t3")
q.appendleft("urgent")
print(q.popleft(), q.popleft(), q)
q.rotate(1)
print(q)

recent = deque(maxlen=3)
for page in ["home", "about", "blog", "contact", "faq"]:
    recent.append(page)
    print("recent pages:", list(recent))

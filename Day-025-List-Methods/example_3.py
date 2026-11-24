# Day 025 · List Methods — Stack and queue with lists
# Run: python example_3.py

stack = []
for item in ["a", "b", "c"]:
    stack.append(item)
print("Stack pop order:", stack.pop(), stack.pop(), stack.pop())

tasks = ["t1", "t2", "t3"]
print("index of t2:", tasks.index("t2"))
print("count of t1:", tasks.count("t1"))
tasks.reverse()
print(tasks)
# For real queues use collections.deque (Level 2)

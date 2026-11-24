# Day 063 · time and calendar Modules — A countdown timer and stopwatch
# Run: python example_3.py

import time

def countdown(seconds):
    while seconds >= 0:
        mins, secs = divmod(seconds, 60)
        print(f"\r⏳ {mins:02d}:{secs:02d}", end="", flush=True)
        time.sleep(0.2)                      # use 1 second for a real timer
        seconds -= 1
    print("\n⏰ Time's up!")

countdown(3)
laps, start = [], time.perf_counter()
for _ in range(3):
    time.sleep(0.1)
    laps.append(time.perf_counter() - start)
print("laps:", [f"{l:.2f}s" for l in laps])

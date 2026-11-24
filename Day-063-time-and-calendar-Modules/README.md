# Day 063 · time and calendar Modules

_Intermediate_

## time
| Function | Use |
|----------|-----|
| `time.time()` | seconds since 1 Jan 1970 (the "epoch") |
| `time.sleep(s)` | pause the program |
| `time.perf_counter()` | precise timer for measuring code |
| `time.monotonic()` | a clock that never goes backwards |
| `time.localtime()`, `time.gmtime()` | struct_time |
| `time.strftime(fmt)` | format a time |
| `time.ctime()` | a readable string |

## calendar
`calendar.month(y, m)`, `calendar.calendar(y)`, `calendar.isleap(y)`, `calendar.monthrange(y, m)`, `calendar.weekday(y, m, d)`, `calendar.day_name`

**Use `datetime` for date maths, `time` for timing and sleeping, and `calendar` for calendars.**

## Examples

### Example 1: The time module  ([`example_1.py`](example_1.py))

```python
import time

print("epoch seconds:", round(time.time()))
print("now:", time.ctime())
print(time.strftime("%d-%m-%Y %H:%M:%S", time.localtime()))
start = time.perf_counter()
time.sleep(0.3)
print(f"slept {time.perf_counter() - start:.3f}s")
t = time.localtime()
print("year:", t.tm_year, "day of year:", t.tm_yday)
```

### Example 2: The calendar module  ([`example_2.py`](example_2.py))

```python
import calendar

print(calendar.month(2026, 11))
print("2028 leap?", calendar.isleap(2028), "| leap years 2000-2030:", calendar.leapdays(2000, 2030))
first_weekday, days = calendar.monthrange(2026, 2)
print("Feb 2026 starts on", calendar.day_name[first_weekday], "and has", days, "days")
print("13 Jan 1998 was a", calendar.day_name[calendar.weekday(1998, 1, 13)])
```

### Example 3: A countdown timer and stopwatch  ([`example_3.py`](example_3.py))

```python
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
```

## Practice

1. Print the calendar for your birth month and year.
2. Build a Pomodoro timer (25 minutes of work, 5 minutes of break).
3. Count how many Fridays fall on the 13th in 2026.

---

[⬅ Day 062](../Day-062-datetime-and-Time-Zones/README.md) · [🏠 Home](../README.md) · [Day 064 ➡](../Day-064-math-random-and-statistics/README.md)

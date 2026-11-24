# 055 · datetime and Time Zones — Example 1: Dates, times and formatting
# Run: python example_1.py

from datetime import date, datetime

today = date(2026, 11, 24)
print(today, today.year, today.strftime("%A, %d %B %Y"))
dt = datetime(2026, 11, 24, 17, 43)
print(dt.strftime("%d/%m/%Y %I:%M %p"))
parsed = datetime.strptime("13-01-1998 04:55", "%d-%m-%Y %H:%M")
print(parsed, parsed.isoformat())

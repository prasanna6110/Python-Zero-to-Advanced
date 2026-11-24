# Day 063 · time and calendar Modules — The calendar module
# Run: python example_2.py

import calendar

print(calendar.month(2026, 11))
print("2028 leap?", calendar.isleap(2028), "| leap years 2000-2030:", calendar.leapdays(2000, 2030))
first_weekday, days = calendar.monthrange(2026, 2)
print("Feb 2026 starts on", calendar.day_name[first_weekday], "and has", days, "days")
print("13 Jan 1998 was a", calendar.day_name[calendar.weekday(1998, 1, 13)])

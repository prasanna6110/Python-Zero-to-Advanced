# Day 062 · datetime and Time Zones — timedelta arithmetic
# Run: python example_2.py

from datetime import date, timedelta

birth = date(1998, 1, 13)
on = date(2026, 11, 24)
age_days = (on - birth).days
print("Days lived:", age_days, "≈ years:", age_days // 365)
print("100 days later:", on + timedelta(days=100))
print("Last week:", on - timedelta(weeks=1))
next_bday = birth.replace(year=on.year)
if next_bday < on:
    next_bday = next_bday.replace(year=on.year + 1)
print("Days to next birthday:", (next_bday - on).days)

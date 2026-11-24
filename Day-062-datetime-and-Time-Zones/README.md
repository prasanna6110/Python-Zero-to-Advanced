# Day 062 · datetime and Time Zones

_Intermediate_

## The datetime module
| Class | Represents |
|-------|-----------|
| `date` | year, month, day |
| `time` | hour, minute, second |
| `datetime` | a date and a time together |
| `timedelta` | a duration (difference between two times) |
| `timezone` / `zoneinfo.ZoneInfo` | a time zone |

## Formatting and parsing
- `dt.strftime("%d-%m-%Y %H:%M")` turns a datetime into a string.
- `datetime.strptime("13-01-1998", "%d-%m-%Y")` turns a string into a datetime.
- `dt.isoformat()` and `datetime.fromisoformat()` use the standard ISO format.

| Code | Meaning |
|------|---------|
| `%Y %m %d` | year, month, day |
| `%H %M %S` | hour, minute, second |
| `%A %B` | weekday name, month name |

**Tip:** store times in UTC and convert them to local time only when you display them.

## Examples

### Example 1: Dates, times and formatting  ([`example_1.py`](example_1.py))

```python
from datetime import date, datetime

today = date(2026, 11, 24)
print(today, today.year, today.strftime("%A, %d %B %Y"))
dt = datetime(2026, 11, 24, 17, 43)
print(dt.strftime("%d/%m/%Y %I:%M %p"))
parsed = datetime.strptime("13-01-1998 04:55", "%d-%m-%Y %H:%M")
print(parsed, parsed.isoformat())
```

### Example 2: timedelta arithmetic  ([`example_2.py`](example_2.py))

```python
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
```

### Example 3: Time zones with zoneinfo  ([`example_3.py`](example_3.py))

```python
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

utc_now = datetime(2026, 11, 24, 12, 13, tzinfo=timezone.utc)
for zone in ["Asia/Kolkata", "America/New_York", "Europe/London", "Asia/Tokyo"]:
    local = utc_now.astimezone(ZoneInfo(zone))
    print(f"{zone:<18} {local:%Y-%m-%d %H:%M %Z}")
```

## Practice

1. Calculate your exact age in years, months and days.
2. List every Sunday in December 2026.
3. Convert a meeting time from IST to 3 other time zones.

---

[⬅ Day 061](../Day-061-Advanced-Sorting/README.md) · [🏠 Home](../README.md) · [Day 063 ➡](../Day-063-time-and-calendar-Modules/README.md)

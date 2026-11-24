# 055 · datetime and Time Zones — Example 3: Time zones with zoneinfo
# Run: python example_3.py

from datetime import datetime, timezone
from zoneinfo import ZoneInfo

utc_now = datetime(2026, 11, 24, 12, 13, tzinfo=timezone.utc)
for zone in ["Asia/Kolkata", "America/New_York", "Europe/London", "Asia/Tokyo"]:
    local = utc_now.astimezone(ZoneInfo(zone))
    print(f"{zone:<18} {local:%Y-%m-%d %H:%M %Z}")

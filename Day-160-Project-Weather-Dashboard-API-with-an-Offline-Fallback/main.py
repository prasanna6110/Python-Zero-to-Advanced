# Day 160 · Project: Weather Dashboard (API with an Offline Fallback) — Weather Dashboard
# Run: python main.py

import json
import sys
import time
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import urlopen

DEMO = not sys.stdin.isatty()
CITIES = {"kurukshetra": (29.97, 76.88), "delhi": (28.61, 77.21), "satna": (24.58, 80.83), "mumbai": (19.08, 72.88)}
CACHE = Path("weather_cache.json")
CODES = {0: "☀️ Clear", 1: "🌤 Mostly clear", 2: "⛅ Partly cloudy", 3: "☁️ Overcast", 45: "🌫 Fog",
         61: "🌧 Rain", 63: "🌧 Rain", 80: "🌦 Showers", 95: "⛈ Thunderstorm"}
SAMPLE = {"current": {"temperature_2m": 21.4, "relative_humidity_2m": 58, "wind_speed_10m": 7.2, "weather_code": 1},
          "daily": {"time": ["2026-11-24", "2026-11-25", "2026-11-26"], "temperature_2m_max": [24.1, 23.5, 22.8],
                    "temperature_2m_min": [9.8, 10.4, 9.1], "weather_code": [1, 2, 0]}}

def fetch(city):
    lat, lon = CITIES[city]
    params = urlencode({"latitude": lat, "longitude": lon, "timezone": "Asia/Kolkata", "forecast_days": 3,
                        "current": "temperature_2m,relative_humidity_2m,wind_speed_10m,weather_code",
                        "daily": "temperature_2m_max,temperature_2m_min,weather_code"})
    cache = json.loads(CACHE.read_text()) if CACHE.exists() else {}
    if city in cache and time.time() - cache[city]["saved"] < 1800:
        return cache[city]["data"], "cache"
    try:
        with urlopen(f"https://api.open-meteo.com/v1/forecast?{params}", timeout=5) as r:
            data = json.loads(r.read())
        cache[city] = {"saved": time.time(), "data": data}
        if not DEMO:
            CACHE.write_text(json.dumps(cache))
        return data, "live"
    except Exception as e:
        return SAMPLE, f"sample (offline: {type(e).__name__})"

def dashboard(city):
    data, source = fetch(city)
    cur, daily = data["current"], data["daily"]
    print(f"\n🌍 {city.title()}  [data: {source}]")
    print(f"   Now: {cur['temperature_2m']}°C {CODES.get(cur['weather_code'], '🌡')}  "
          f"humidity {cur['relative_humidity_2m']}%  wind {cur['wind_speed_10m']} km/h")
    for day, hi, lo, code in zip(daily["time"], daily["temperature_2m_max"], daily["temperature_2m_min"], daily["weather_code"]):
        bar = " " * int(lo) + "▬" * int(hi - lo)
        print(f"   {day}  {lo:>5.1f}° {bar[:40]} {hi:.1f}°  {CODES.get(code, '')}")

if __name__ == "__main__":
    cities = ["kurukshetra", "satna"] if DEMO else [input(f"City {list(CITIES)}: ").strip().lower() or "delhi"]
    for c in cities:
        dashboard(c if c in CITIES else "delhi")

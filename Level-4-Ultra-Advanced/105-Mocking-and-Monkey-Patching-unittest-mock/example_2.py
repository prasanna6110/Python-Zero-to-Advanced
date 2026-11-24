# 105 · Mocking and Monkey Patching (unittest.mock) — Example 2: patch: replacing network calls in tests
# Run: python example_2.py

import unittest
from unittest.mock import patch
import urllib.request, json

def get_weather(city):
    with urllib.request.urlopen(f"https://api.weather.example/{city}") as r:
        data = json.loads(r.read())
    return f"{city}: {data['temp']}°C"

class TestWeather(unittest.TestCase):
    @patch("urllib.request.urlopen")
    def test_weather(self, mock_urlopen):
        mock_urlopen.return_value.__enter__.return_value.read.return_value = b'{"temp": 22}'
        self.assertEqual(get_weather("Kurukshetra"), "Kurukshetra: 22°C")
        mock_urlopen.assert_called_once()

    def test_time_freeze(self):
        with patch("time.time", return_value=1_700_000_000):
            import time
            self.assertEqual(time.time(), 1_700_000_000)

if __name__ == "__main__":
    unittest.main(verbosity=2)

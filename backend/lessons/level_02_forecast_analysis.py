"""
INSTRUCTIONS:
Complete TODOs 1-4 in backend/weather_logic.py.
Run this file after each function. The checks below should eventually pass.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from sample_weather import SAMPLE_WEATHER
from weather_logic import (
    calculate_average_temperature,
    find_coldest_day,
    find_hottest_day,
    find_wettest_day,
)

forecast = SAMPLE_WEATHER["Kigali"]["forecast"]
print("LEVEL 2: Forecast Analysis")
print("-" * 50)

try:
    hottest = find_hottest_day(forecast)
    coldest = find_coldest_day(forecast)
    average = calculate_average_temperature(forecast)
    wettest = find_wettest_day(forecast)
except NotImplementedError as error:
    print("A forecast function is still waiting for your code:")
    print(error)
    raise SystemExit

print("Hottest day:", hottest["date"])
print("Coldest day:", coldest["date"])
print("Average high:", average)
print("Wettest day:", wettest["date"])

print("\nCHECKING LEVEL 2...")
assert hottest["date"] == "2026-10-19"
assert coldest["date"] == "2026-10-18"
assert average == 27.0
assert wettest["date"] == "2026-10-20"
print("Excellent! Your forecast analysis is working.")
print("LEVEL 2 COMPLETE: You can now build weather decisions!\n")

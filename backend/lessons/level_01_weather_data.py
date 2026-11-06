"""
INSTRUCTIONS:
Explore the provided weather notebook. Run this file before changing code.
There is no TODO here because the sample data is already complete.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from sample_weather import SAMPLE_WEATHER

print("LEVEL 1: Exploring Weather Data")
print("-" * 50)

print("Available cities:", ", ".join(SAMPLE_WEATHER))
city = SAMPLE_WEATHER["Kigali"]
print("City:", city["city"])
print("Country:", city["country"])
print("Current temperature:", city["current"]["temperature"], "C")
print("First forecast day:", city["forecast"][0]["date"])
print("First forecast high:", city["forecast"][0]["temperature_max"], "C")

print("\nCHECKING LEVEL 1...")
if isinstance(city, dict) and isinstance(city["forecast"], list):
    print("Great job! You found a dictionary and a list.")
    print("LEVEL 1 COMPLETE: You are ready to analyze forecasts!\n")
else:
    print("Check that city data is a dictionary and forecast data is a list.")

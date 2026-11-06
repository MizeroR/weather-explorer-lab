"""
INSTRUCTIONS:
Complete TODOs 6-8 in backend/weather_service.py.
This level uses the internet. Run it after the offline levels pass.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from weather_service import find_city, get_weather_for_city

print("LEVEL 4: Connecting to Open-Meteo")
print("-" * 50)

try:
    city = find_city("Kigali")
    weather = get_weather_for_city("Kigali")
except NotImplementedError as error:
    print("An API function is still waiting for your code:")
    print(error)
    raise SystemExit
except Exception as error:
    print("The API request could not be completed:")
    print(error)
    raise SystemExit

print("City result:", city)
print("Forecast days returned:", len(weather["forecast"]))
print("\nCHECKING LEVEL 4...")
assert city["city"]
assert len(weather["forecast"]) == 5
print("Fantastic! Open-Meteo data is ready for Flask.")
print("LEVEL 4 COMPLETE: The weather service is ready!\n")

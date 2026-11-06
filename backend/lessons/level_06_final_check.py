"""
INSTRUCTIONS:
Run this final check after completing TODOs 1-11.
Then open the frontend in demo mode and live mode for your presentation.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app import app

print("LEVEL 6: Final Weather Explorer Check")
print("-" * 50)
client = app.test_client()

health = client.get("/api/health")
weather = client.get("/api/weather?city=Kigali")
forecast = client.get("/api/forecast?city=Kigali")
umbrella = client.get("/api/umbrella?city=Kigali")

print("Health status:", health.status_code)
print("Weather status:", weather.status_code)
print("Forecast status:", forecast.status_code)
print("Umbrella status:", umbrella.status_code)

print("\nCHECKING LEVEL 6...")
assert health.status_code == 200
if 501 in (weather.status_code, forecast.status_code, umbrella.status_code):
    print("Some Flask TODOs are still unfinished. Complete TODOs 9-11, then run again.")
    raise SystemExit

assert weather.status_code == 200
assert forecast.status_code == 200
assert umbrella.status_code == 200
print("All core Flask routes returned successfully.")
print("LEVEL 6 COMPLETE: Present your Weather Explorer project!\n")

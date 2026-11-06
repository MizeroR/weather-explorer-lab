"""
INSTRUCTIONS:
Complete TODO 6 in backend/weather_logic.py.
The recommendation uses a 40 percent threshold and must explain its decision.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from weather_logic import umbrella_recommendation

print("LEVEL 3: Umbrella Challenge")
print("-" * 50)

try:
    likely = umbrella_recommendation(65)
    unlikely = umbrella_recommendation(20)
    unknown = umbrella_recommendation(None)
except NotImplementedError as error:
    print("The umbrella function is still waiting for your code:")
    print(error)
    raise SystemExit

print("At 65 percent:", likely)
print("At 20 percent:", unlikely)
print("With missing data:", unknown)

print("\nCHECKING LEVEL 3...")
assert likely["bring_umbrella"] is True
assert unlikely["bring_umbrella"] is False
assert "unknown" in unknown["recommendation"].lower()
print("Nice work! Your weather rule explains its decision.")
print("LEVEL 3 COMPLETE: The Umbrella Challenge is ready!\n")

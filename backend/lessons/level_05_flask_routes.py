"""
INSTRUCTIONS:
Complete TODOs 9-11 in backend/app.py after the weather service works.
This file checks the Flask boundary without starting a web server.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app import app

print("LEVEL 5: Connecting Flask Routes")
print("-" * 50)
client = app.test_client()

health = client.get("/api/health")
print("Health response:", health.get_json())

print("\nCHECKING LEVEL 5...")
assert health.status_code == 200
assert health.get_json()["status"] == "ok"
print("The Flask server boundary is healthy.")
print("The weather and forecast routes should return 501 until TODOs 9-11 are complete.")
print("LEVEL 5 COMPLETE when the route checks and full tests pass!\n")

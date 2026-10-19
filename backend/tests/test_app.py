"""Runnable checks for the scaffolded Flask boundary."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1]))

from app import app


def test_health_endpoint():
    client = app.test_client()
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "ok"


def test_weather_requires_city():
    response = app.test_client().get("/api/weather")
    assert response.status_code == 400


def test_unfinished_route_is_explicit():
    response = app.test_client().get("/api/weather?city=Kigali")
    assert response.status_code == 501

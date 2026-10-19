"""Fictional teaching data for offline Weather Explorer exercises."""

SAMPLE_WEATHER = {
    "Kigali": {
        "city": "Kigali",
        "country": "Rwanda",
        "latitude": -1.9441,
        "longitude": 30.0619,
        "current": {"temperature": 24.5, "wind_speed": 9.2, "weather_code": 2},
        "forecast": [
            {"date": "2026-10-16", "temperature_max": 27, "temperature_min": 17, "precipitation_probability": 35},
            {"date": "2026-10-17", "temperature_max": 28, "temperature_min": 18, "precipitation_probability": 55},
            {"date": "2026-10-18", "temperature_max": 26, "temperature_min": 16, "precipitation_probability": 20},
            {"date": "2026-10-19", "temperature_max": 29, "temperature_min": 18, "precipitation_probability": 45},
            {"date": "2026-10-20", "temperature_max": 25, "temperature_min": 17, "precipitation_probability": 65},
        ],
    },
    "Nairobi": {
        "city": "Nairobi", "country": "Kenya", "latitude": -1.2864, "longitude": 36.8172,
        "current": {"temperature": 22.1, "wind_speed": 12.4, "weather_code": 3},
        "forecast": [
            {"date": "2026-10-16", "temperature_max": 25, "temperature_min": 14, "precipitation_probability": 25},
            {"date": "2026-10-17", "temperature_max": 24, "temperature_min": 15, "precipitation_probability": 40},
            {"date": "2026-10-18", "temperature_max": 26, "temperature_min": 14, "precipitation_probability": 15},
            {"date": "2026-10-19", "temperature_max": 23, "temperature_min": 13, "precipitation_probability": 70},
            {"date": "2026-10-20", "temperature_max": 25, "temperature_min": 14, "precipitation_probability": 30},
        ],
    },
    "London": {
        "city": "London", "country": "United Kingdom", "latitude": 51.5072, "longitude": -0.1276,
        "current": {"temperature": 13.8, "wind_speed": 16.1, "weather_code": 61},
        "forecast": [
            {"date": "2026-10-16", "temperature_max": 16, "temperature_min": 10, "precipitation_probability": 75},
            {"date": "2026-10-17", "temperature_max": 15, "temperature_min": 9, "precipitation_probability": 60},
            {"date": "2026-10-18", "temperature_max": 17, "temperature_min": 11, "precipitation_probability": 35},
            {"date": "2026-10-19", "temperature_max": 14, "temperature_min": 8, "precipitation_probability": None},
            {"date": "2026-10-20", "temperature_max": 18, "temperature_min": 12},
        ],
    },
}

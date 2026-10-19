"""Starter functions for Open-Meteo requests.

Builders implement these after practicing dictionaries and JSON with sample data.
Official docs: https://open-meteo.com/en/docs and https://open-meteo.com/en/docs/geocoding-api
"""

import requests

GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
FORECAST_URL = "https://api.open-meteo.com/v1/forecast"
REQUEST_TIMEOUT = 10


# TODO 11: backend/weather_service.py -> find_city
# Validate city_name, then call GEOCODING_URL with params
# {"name": city_name, "count": 1, "language": "en", "format": "json"}.
# Call response.raise_for_status(), inspect the results list, and return only
# name, country, latitude, and longitude. Expected result: find_city("Kigali")
# returns those four keys. Handle blank names, no results, timeouts, and
# requests.RequestException.
def find_city(city_name):
    """Find a city and return name, country, latitude, and longitude.

    Implementation note: validate the name, call GEOCODING_URL with name and count parameters,
    check the response, and select the first result. Consider empty results,
    timeouts, and requests.RequestException.
    """
    raise NotImplementedError("Builder task: implement Open-Meteo geocoding")


# TODO 12: backend/weather_service.py -> get_weather
# Call FORECAST_URL with latitude, longitude, timezone=auto,
# forecast_days=5, current weather fields, and daily fields including time,
# temperature_2m_max, temperature_2m_min, precipitation_probability_max, and
# wind_speed_10m_max. Convert Open-Meteo's parallel daily lists into five day
# dictionaries matching sample_weather.py. Expected result: five forecast
# dictionaries with date, high, low, and precipitation keys. Handle failures.
def get_weather(latitude, longitude):
    """Retrieve current weather and daily forecast for coordinates.

    Implementation note: call FORECAST_URL with latitude, longitude, current fields, daily fields,
    timezone=auto, and forecast_days=5. Use REQUEST_TIMEOUT and handle HTTP errors.
    Return a normalized dictionary that weather_logic functions can understand.
    """
    raise NotImplementedError("Builder task: implement Open-Meteo forecast retrieval")


# TODO 13: backend/weather_service.py -> get_weather_for_city
# Call find_city(city_name), pass its coordinates to
# get_weather, then add the selected city and country to the returned record.
# This function should be the one Flask calls for a city's complete weather.
# Expected result: one normalized record containing city, country, current, and forecast.
def get_weather_for_city(city_name):
    """Combine city search and weather retrieval into one reusable operation."""
    raise NotImplementedError("Builder task: combine find_city and get_weather")

"""Starter functions for Open-Meteo requests.

Students implement these after practicing dictionaries and JSON with sample data.
Official docs: https://open-meteo.com/en/docs and https://open-meteo.com/en/docs/geocoding-api
"""

import requests

GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
FORECAST_URL = "https://api.open-meteo.com/v1/forecast"
REQUEST_TIMEOUT = 10


def find_city(city_name):
    """Find a city and return name, country, latitude, and longitude.

    TODO: validate the name, call GEOCODING_URL with name and count parameters,
    check the response, and select the first result. Consider empty results,
    timeouts, and requests.RequestException.
    """
    raise NotImplementedError("Student task: implement Open-Meteo geocoding")


def get_weather(latitude, longitude):
    """Retrieve current weather and daily forecast for coordinates.

    TODO: call FORECAST_URL with latitude, longitude, current fields, daily fields,
    timezone=auto, and forecast_days=5. Use REQUEST_TIMEOUT and handle HTTP errors.
    Return a normalized dictionary that weather_logic functions can understand.
    """
    raise NotImplementedError("Student task: implement Open-Meteo forecast retrieval")


def get_weather_for_city(city_name):
    """Combine city search and weather retrieval into one reusable operation."""
    raise NotImplementedError("Student task: combine find_city and get_weather")

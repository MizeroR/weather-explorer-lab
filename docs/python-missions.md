# Python Missions

This guide describes the required core path. The frontend is already provided; builders focus on Python.

## How to work

Run one level at a time from the `backend` directory. Open the implementation file named in the level, complete only the numbered TODOs listed there, and run the level again. Read the expected result beside each TODO before writing code.

## Level 1: Explore Weather Data

- **Open:** `backend/sample_weather.py`
- **Practice:** dictionaries, lists, strings, numbers, and missing values.
- **Task:** inspect Kigali's current reading and first forecast day.
- **Expected result:** you can point to the city dictionary, current dictionary, and forecast list.
- **Run:** `python3 lessons/level_01_weather_data.py`

No code change is required. The sample dataset is already provided.

## Level 2: Analyze a Forecast

- **Open:** `backend/weather_logic.py`
- **Complete:** TODOs 1-4.
- **Practice:** loops, comparisons, conditions, and safe missing data.
- **Task:** find the hottest day, coldest day, average high, and wettest day.
- **Expected result:** the Kigali checks pass: hottest `2026-10-19`, coldest `2026-10-18`, average `27.0`, wettest `2026-10-20`.
- **Run:** `python3 lessons/level_02_forecast_analysis.py`

## Level 3: Build the Umbrella Challenge

- **Open:** `backend/weather_logic.py`
- **Complete:** TODO 5.
- **Practice:** functions, thresholds, boolean conditions, and validation.
- **Task:** recommend an umbrella at or above 40% precipitation probability and explain the decision.
- **Expected result:** 40% returns `bring_umbrella=True`, 39% returns `False`, and missing data says the chance is unknown.
- **Run:** `python3 lessons/level_03_umbrella.py`

## Level 4: Connect to Open-Meteo

- **Open:** `backend/weather_service.py`
- **Complete:** TODOs 6-8.
- **Practice:** HTTP requests, query parameters, JSON responses, exceptions, and data normalization.
- **Task:** find a city, retrieve its current weather and five-day forecast, and convert the API response into the sample-data shape.
- **Expected result:** `find_city("Kigali")` returns city information and the weather record contains five forecast dictionaries.
- **Run:** `python3 lessons/level_04_weather_api.py`

This level needs internet access.

## Level 5: Connect Flask

- **Open:** `backend/app.py`
- **Complete:** TODOs 9-11.
- **Practice:** route parameters, JSON responses, validation, and connecting modules.
- **Task:** connect `/api/weather`, `/api/forecast`, and `/api/umbrella` to the service and logic functions.
- **Expected result:** valid requests return HTTP 200 JSON; missing city values return HTTP 400; service failures do not expose tracebacks.
- **Run:** `python3 lessons/level_05_flask_routes.py`

## Level 6: Test and Present

- **Open:** `backend/tests/` and the frontend.
- **Practice:** automated testing, debugging, and explaining a program.
- **Task:** run the complete test suite, check the frontend in demo mode, start Flask, and check live mode.
- **Expected result:** all core tests pass, the frontend shows sample data offline, and live mode displays Open-Meteo data after the Flask routes are complete.
- **Run:** `python3 lessons/level_06_final_check.py`, then `python3 -m pytest -q`.

## Optional extensions

Only attempt these after the core project works:

- Compare two cities.
- Add a chart-ready data function.
- Add a weather quiz.
- Add a new city to the sample dataset.
- Let the builder change the umbrella threshold.

# Python Missions

Work through these missions in order. The interface is already provided; your job as the builder is to make the Python ideas underneath it work.

## How to use this guide

For every mission, open the file named under **Edit**, find the uniquely numbered TODO named under **Task**, and replace its `NotImplementedError` with your own code. Read the expected result in the TODO comment before coding. Run the focused test command after each small change. Do not edit `frontend/` for the core missions.

The normal rhythm is: read the docstring, inspect the sample data, write a small piece of Python, run one focused test, use the error message, and repeat. Start with `backend/weather_logic.py`; leave `backend/weather_service.py` until you are comfortable with dictionaries, lists, loops, and conditions.

## 1. Explore the Weather Station
**Story:** You have inherited a weather notebook from a field scientist.

- **Concepts:** variables, strings, numbers, dictionaries, lists.
- **Edit:** `backend/sample_weather.py` only to inspect or add teaching data.
- **Task:** print a city's name, current temperature, and first forecast day. This is an Explore step, not a TODO.
- **Expected behavior:** your program reads values from nested dictionaries without changing the data shape.
- **Checklist:** identify keys; identify list indexes; handle a missing key safely.
- **Bonus:** add a fourth fictional station.
- **Start command:** `python -c "from backend.sample_weather import SAMPLE_WEATHER; print(SAMPLE_WEATHER['Kigali'])"`

## 2. Understand JSON
- **Concepts:** JSON-shaped data and data transformation.
- **Edit:** a scratch copy or Python REPL; then `backend/weather_logic.py`.
- **Task:** explain the difference between a dictionary and a list by inspecting the sample forecast.
- **Expected behavior:** you can describe which values are strings, numbers, lists, and `None`.
- **Checklist:** find one missing value; write one small function that reads a key.
- **Bonus:** turn one forecast day into a sentence.
- **Done when:** you can point to a dictionary, list, string, number, and missing `None` value.

## 3. Find a City Using an API
- **Concepts:** functions, requests, query parameters, JSON responses, exceptions.
- **Edit:** `backend/weather_service.py`.
- **Task:** implement `find_city` using the Open-Meteo geocoding URL.
- **Expected behavior:** a valid city returns name, country, latitude, and longitude; an unknown city gives a useful error.
- **Checklist:** validate input; use a timeout; check HTTP errors; handle no results.
- **Bonus:** allow a result-count parameter.

## 4. Retrieve and Process Weather Data
- **Concepts:** API parameters, nested JSON, normalization.
- **Edit:** `backend/weather_service.py`.
- **Task:** implement `get_weather` and `get_weather_for_city` with five daily records.
- **Expected behavior:** the service returns the same shape as `sample_weather.py`.
- **Checklist:** request current and daily values; preserve missing values; catch request failures.
- **Bonus:** add a readable weather-code label.

## 5. Analyze the Forecast
- **Concepts:** loops, conditions, comparisons, safe missing data.
- **Edit:** `backend/weather_logic.py`.
- **Task:** implement TODO 1, TODO 2, TODO 3, and TODO 4: hottest, coldest, average, and wettest-day functions.
- **Expected behavior:** the tests for `ForecastAnalysisTests` pass, including incomplete records.
- **Checklist:** decide what an empty list should do; skip `None`; use meaningful names.
- **Bonus:** calculate the temperature range.
- **Edit these exact TODOs:** TODO 1, TODO 2, TODO 3, and TODO 4 in `backend/weather_logic.py`.
- **Test command:** `python -m pytest -q backend/tests/test_weather_logic.py -k ForecastAnalysis`.

## 6. Build the Umbrella Challenge
- **Concepts:** boolean conditions, thresholds, validation.
- **Edit:** `backend/weather_logic.py`, then the umbrella route in `backend/app.py`.
- **Task:** implement TODO 6, `umbrella_recommendation`, with a configurable 40% default.
- **Expected behavior:** 40% recommends an umbrella, 39% does not, and missing data explains uncertainty.
- **Checklist:** validate numeric input; return an understandable dictionary; mention this is a rule.
- **Bonus:** make the threshold configurable in the UI request.
- **Edit these exact locations:** TODO 6 in `weather_logic.py`; the route connection happens later at TODO 17 in `app.py`.
- **Test command:** `python -m pytest -q backend/tests/test_weather_logic.py -k Umbrella`.

## 7. Compare Two Cities
- **Concepts:** function arguments, conditions, composing dictionaries.
- **Edit:** `backend/weather_logic.py`, then the compare route.
- **Task:** implement TODO 5: compare temperature, wind, and precipitation when values exist.
- **Expected behavior:** the result clearly identifies warmer and windier cities without crashing on missing values.
- **Checklist:** test equal values; test missing precipitation; avoid duplicate API calls.
- **Bonus:** compare average forecast temperatures.
- **Edit these exact locations:** TODO 5 in `weather_logic.py`; the route connection happens later at TODO 16 in `app.py`.
- **Test command:** `python -m pytest -q backend/tests/test_weather_logic.py -k Comparison`.

## 8. Become a Weather Scientist
- **Concepts:** data transformation and chart-ready lists.
- **Edit:** `prepare_scientist_data` and `summarize_forecast`.
- **Task:** produce labels, high temperatures, and precipitation probabilities for the frontend.
- **Expected behavior:** parallel lists have the same length and a summary is readable.
- **Checklist:** handle empty input; preserve dates; calculate an average.
- **Bonus:** identify the biggest temperature swing.
- **Edit these exact TODOs:** TODO 7 and TODO 8 in `weather_logic.py`.
- **Manual check:** call each function with `SAMPLE_WEATHER['Kigali']['forecast']` and inspect the result.

## 9. Add Quiz Scoring
- **Concepts:** string cleanup, list iteration, validation.
- **Edit:** TODO 9 and TODO 10 in `weather_logic.py`; the route connection happens later at TODO 18 in `app.py`.
- **Task:** compare answers without being fussy about capitalization or surrounding spaces.
- **Expected behavior:** the quiz tests pass and invalid submissions receive a helpful response.
- **Checklist:** decide how to handle unequal list lengths; test blank answers.
- **Bonus:** return feedback for each question.
- **Edit these exact locations:** TODO 9, TODO 10, and TODO 18.
- **Test command:** `python -m pytest -q backend/tests/test_weather_logic.py -k Quiz`.

## 10. Test, Debug, and Present
- **Concepts:** unit tests, test clients, debugging, Git.
- **Edit:** add tests in `backend/tests/` and finish remaining Flask routes.
- **Task:** run all tests, investigate failures, and demonstrate mock and live modes.
- **Expected behavior:** your completed features work offline with sample data and online with Open-Meteo.
- **Checklist:** run `python -m pytest -q`; check `/api/health`; explain one design choice.
- **Bonus:** add a new test before adding a new feature.
- **Final commands:** `python -m pytest -q backend/tests/test_app.py`, then `python -m pytest -q`.

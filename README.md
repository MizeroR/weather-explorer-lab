# Weather Explorer Lab: Build, Predict & Discover

A Python-first weather science project exercise. The frontend is ready to explore in demo mode; the builder will build the weather service, analysis logic, and API routes in Python.

## What is already working?

- The frontend works without Flask or internet access.
- Demo data includes Kigali, Nairobi, and London.
- Search, forecast cards, umbrella display, chart, quiz interaction, loading status, and errors work in demo mode.
- The Flask app starts and `/api/health` works.

## What to implement

The intentional `TODO 1` through `TODO 18` tasks are in `backend/weather_logic.py`, `backend/weather_service.py`, and `backend/app.py`. Each number appears once in the project. Open the matching file, read the expected result beside the TODO, write the code, and run the focused check before moving on.

## Start here: your Python path

You do **not** need to edit the frontend for the core project. Follow this order:

| Step | Open this file | Complete these TODOs | Check your work |
| --- | --- | --- | --- |
| 1 | `backend/sample_weather.py` | Explore the provided data. No TODO is needed here. | Print a city, temperature, and forecast day. |
| 2 | `backend/weather_logic.py` | Complete TODO 1-4: forecast analysis. | `python -m pytest -q backend/tests/test_weather_logic.py -k ForecastAnalysis` |
| 3 | `backend/weather_logic.py` | Complete TODO 5: city comparison. | `python -m pytest -q backend/tests/test_weather_logic.py -k Comparison` |
| 4 | `backend/weather_logic.py` | Complete TODO 6: umbrella recommendation. | `python -m pytest -q backend/tests/test_weather_logic.py -k Umbrella` |
| 5 | `backend/weather_logic.py` | Complete TODO 7-8: scientist data and summary. | Call both functions with the sample forecast. |
| 6 | `backend/weather_logic.py` | Complete TODO 9-10: quiz answer and score. | `python -m pytest -q backend/tests/test_weather_logic.py -k Quiz` |
| 7 | `backend/weather_service.py` | Complete TODO 11-13: city search and weather retrieval. | Test a real city and mocked failures. |
| 8 | `backend/app.py` | Complete TODO 14-18: connect Flask routes. | Run endpoint tests and `curl` requests. |
| 9 | `backend/tests/` | Add edge-case checks after the core work passes. | `python -m pytest -q` |

The frontend is your **viewer**. Its demo calculations are provided so the interface works offline; your assignment is to recreate the underlying calculations in Python and connect them through Flask.

### How to recognize an unfinished task

- A function containing `raise NotImplementedError("Builder task: ...")` is waiting for your code.
- A route returning HTTP `501` is scaffolded but not connected yet.
- A test failure mentioning `NotImplementedError` usually means the next TODO has not been implemented.
- A passing frontend demo does not mean the Python mission is complete.

### Your first 15 minutes

1. Run the demo frontend and search for Kigali, Nairobi, and London.
3. Open `backend/sample_weather.py` and identify its dictionaries and forecast list.
4. Open `backend/weather_logic.py` and complete TODO 1 only.
5. Run `python -m pytest -q backend/tests/test_weather_logic.py -k test_finds_hottest_day`.
5. Read the next failing function and continue one function at a time.

The full explanations and checklists are in [docs/python-missions.md](docs/python-missions.md).

## Learning goals

Practice variables, dictionaries, lists, loops, conditions, functions, JSON, HTTP requests, exceptions, validation, data transformation, testing, and simple decision rules.

## Requirements

Install Python 3.10 or newer. A browser is enough for demo mode. Git is recommended. No Node.js, React, database, or authentication is needed.

## Get the project

```bash
git clone YOUR_REPOSITORY_URL
cd weather-explorer-lab
```

## Run the frontend in demo mode

The frontend is a normal static website. Open `frontend/index.html` in a browser, or serve the repository with Python:

```bash
python -m http.server 5500 --directory frontend
```

Visit <http://localhost:5500>. It displays a `DEMO DATA` label and does not need Flask.

## Set up Python

macOS/Linux:

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Windows PowerShell:

```powershell
cd backend
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Windows Command Prompt uses `.venv\Scripts\activate.bat` instead.

## Start Flask

With the virtual environment active:

```bash
python app.py
```

In another terminal, verify the implemented scaffold:

```bash
curl http://localhost:5000/api/health
```

You should receive JSON containing `"status": "ok"`. Routes tied to unfinished TODOs intentionally return HTTP 501 until the builder implements them.

## Switch to live mode

Keep the Flask server on port 5000 and the frontend server on port 5500. Open `http://localhost:5500`, then select **Switch to live**. The frontend calls `GET /api/weather?city=...`; it shows `LIVE DATA` only after a successful backend response. A failed live request is shown as an error and is never silently replaced with demo data.

The remaining live routes are already named in `frontend/js/app.js` and scaffolded in Flask for the builder to connect as TODOs are completed: forecast, compare, umbrella, and quiz.

## Run tests

The project uses `unittest` for the starter checks and `pytest` is included for convenient test output:

```bash
python -m pytest -q
```

To run only the already-implemented Flask scaffold checks:

```bash
python -m pytest -q backend/tests/test_app.py
```

The scaffold tests in `test_app.py` should pass. The weather-logic tests are deliberately red while the builder functions raise `NotImplementedError`; that is a sign that the next TODO is waiting, not a broken starter repository.

## Folder map

```text
frontend/index.html              Provided interface
frontend/css/style.css           Visual design and responsive layout
frontend/js/app.js               Demo data and ready-made API calls
backend/app.py                   Flask routes and validation scaffold
backend/weather_service.py       Builder Open-Meteo request tasks
backend/weather_logic.py         Main builder Python exercises
backend/sample_weather.py        Fictional offline practice data
backend/tests/test_app.py        Runnable Flask boundary checks
backend/tests/test_weather_logic.py  Guiding behavior tests
docs/python-missions.md          Mission-by-mission learning guide
```

## Git workflow

Save small milestones:

```bash
git status
git add backend/weather_logic.py
git commit -m "Complete forecast analysis mission"
git push
```

Commit after a mission passes its tests. Never commit `.venv`, API keys, cache folders, or personal editor settings.

## Troubleshooting

- **`python` is not found:** try `python3` on macOS/Linux or `py` on Windows.
- **PowerShell blocks activation:** use `Set-ExecutionPolicy -Scope Process Bypass` for the current terminal, then activate again.
- **Port 5500 is busy:** use another port and update the documented CORS origin in `backend/app.py`.
- **Live mode says it cannot connect:** start Flask, confirm port 5000, and check the browser console.
- **A weather test raises `NotImplementedError`:** that function is an intentional builder task. Read the numbered TODO directly above it.
- **Open-Meteo fails:** check internet access, request parameters, and timeout/error handling. Demo mode remains available offline.

## Final presentation checklist

Demonstrate demo mode, health check, at least three completed Python missions, passing focused tests, clear handling of missing data, one live city lookup, and one thoughtful bonus improvement. Explain how one frontend feature depends on a Python function.

## Extensions

Add a new city to the teaching data, write a new test before a new feature, add a weather-code dictionary, compare forecast averages, or allow the umbrella threshold to be changed by the user. Deployment can use any simple Python host that supports Flask; do not commit secrets or rely on a local-only URL in production.

## Data source

Live data is requested from the free [Open-Meteo Forecast API](https://open-meteo.com/en/docs) and [Geocoding API](https://open-meteo.com/en/docs/geocoding-api). The bundled readings are fictional teaching data and are not live measurements.

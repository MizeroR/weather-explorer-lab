"""Flask starter API for Weather Explorer Lab."""

from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": ["http://localhost:5500", "http://127.0.0.1:5500"]}})


def unfinished_response():
    return jsonify({"error": "This builder feature is not implemented yet.", "hint": "Complete the matching TODO first."}), 501


@app.get("/api/health")
def health():
    return jsonify({"status": "ok", "message": "Weather Explorer Lab backend is running."})


@app.get("/api/weather")
def weather():
    if not request.args.get("city", "").strip():
        return jsonify({"error": "Please provide a city query parameter."}), 400
    # TODO 9: backend/app.py -> GET /api/weather
    # Import get_weather_for_city, call it with city, and jsonify the normalized
    # record. Expected result: GET /api/weather?city=Kigali returns HTTP 200 with
    # city, country, current, and forecast keys. Convert known service failures
    # into useful JSON responses without exposing a traceback.
    return unfinished_response()


@app.get("/api/forecast")
def forecast():
    if not request.args.get("city", "").strip():
        return jsonify({"error": "Please provide a city query parameter."}), 400
    # TODO 10: backend/app.py -> GET /api/forecast
    # Reuse get_weather_for_city rather than making a second API request.
    # Expected result: GET /api/forecast?city=Kigali returns a city and five-day
    # forecast list.
    return unfinished_response()


@app.get("/api/umbrella")
def umbrella():
    if not request.args.get("city", "").strip():
        return jsonify({"error": "Please provide a city query parameter."}), 400
# TODO 11: backend/app.py -> GET /api/umbrella
    # Retrieve the city, find the highest available forecast probability, pass it
    # to umbrella_recommendation, and jsonify the result. Expected result: JSON
    # contains bring_umbrella, recommendation, and explanation.
    return unfinished_response()


if __name__ == "__main__":
    app.run(debug=True, port=5000)

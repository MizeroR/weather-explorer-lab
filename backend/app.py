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
    # TODO 14: backend/app.py -> GET /api/weather
    # Import get_weather_for_city, call it with city, and jsonify the normalized
    # record. Expected result: GET /api/weather?city=Kigali returns HTTP 200 with
    # city, country, current, and forecast keys. Convert known service failures
    # into useful JSON responses without exposing a traceback.
    return unfinished_response()


@app.get("/api/forecast")
def forecast():
    if not request.args.get("city", "").strip():
        return jsonify({"error": "Please provide a city query parameter."}), 400
    # TODO 15: backend/app.py -> GET /api/forecast
    # Reuse get_weather_for_city rather than making a second API request.
    # Expected result: GET /api/forecast?city=Kigali returns a city and five-day
    # forecast list.
    return unfinished_response()


@app.get("/api/compare")
def compare():
    if not request.args.get("city1", "").strip() or not request.args.get("city2", "").strip():
        return jsonify({"error": "Please provide city1 and city2 query parameters."}), 400
    # TODO 16: backend/app.py -> GET /api/compare
    # Retrieve city1 and city2 with the service, then pass both records to
    # weather_logic.compare_cities. Expected result: JSON includes comparison
    # keys such as warmer_city and higher_wind_city. Do not duplicate API code.
    return unfinished_response()


@app.get("/api/umbrella")
def umbrella():
    if not request.args.get("city", "").strip():
        return jsonify({"error": "Please provide a city query parameter."}), 400
    # TODO 17: backend/app.py -> GET /api/umbrella
    # Retrieve the city, find the highest available forecast probability, pass it
    # to umbrella_recommendation, and jsonify the result. Expected result: JSON
    # contains bring_umbrella, recommendation, and explanation.
    return unfinished_response()


@app.post("/api/quiz/check")
def quiz_check():
    body = request.get_json(silent=True)
    if not isinstance(body, dict) or "answers" not in body:
        return jsonify({"error": "Send a JSON object containing an answers list."}), 400
    if not isinstance(body["answers"], list):
        return jsonify({"error": "answers must be a list."}), 400
    # TODO 18: backend/app.py -> POST /api/quiz/check
    # Validate submitted answers, define or load the expected-answer list, call
    # calculate_quiz_score, and return score feedback. Expected result: valid
    # JSON returns a numeric score; invalid JSON returns HTTP 400.
    return unfinished_response()


if __name__ == "__main__":
    app.run(debug=True, port=5000)

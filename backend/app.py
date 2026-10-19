"""Flask starter API for Weather Explorer Lab."""

from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": ["http://localhost:5500", "http://127.0.0.1:5500"]}})


def unfinished_response():
    return jsonify({"error": "This student feature is not implemented yet.", "hint": "Complete the matching Python mission first."}), 501


@app.get("/api/health")
def health():
    return jsonify({"status": "ok", "message": "Weather Explorer Lab backend is running."})


@app.get("/api/weather")
def weather():
    if not request.args.get("city", "").strip():
        return jsonify({"error": "Please provide a city query parameter."}), 400
    # TODO: call weather_service.get_weather_for_city and return its normalized record.
    return unfinished_response()


@app.get("/api/forecast")
def forecast():
    if not request.args.get("city", "").strip():
        return jsonify({"error": "Please provide a city query parameter."}), 400
    # TODO: return the selected city's five-day forecast.
    return unfinished_response()


@app.get("/api/compare")
def compare():
    if not request.args.get("city1", "").strip() or not request.args.get("city2", "").strip():
        return jsonify({"error": "Please provide city1 and city2 query parameters."}), 400
    # TODO: retrieve both cities and pass their records to weather_logic.compare_cities.
    return unfinished_response()


@app.get("/api/umbrella")
def umbrella():
    if not request.args.get("city", "").strip():
        return jsonify({"error": "Please provide a city query parameter."}), 400
    # TODO: retrieve forecast data and pass its precipitation probability to umbrella_recommendation.
    return unfinished_response()


@app.post("/api/quiz/check")
def quiz_check():
    body = request.get_json(silent=True)
    if not isinstance(body, dict) or "answers" not in body:
        return jsonify({"error": "Send a JSON object containing an answers list."}), 400
    if not isinstance(body["answers"], list):
        return jsonify({"error": "answers must be a list."}), 400
    # TODO: validate answers, call weather_logic.calculate_quiz_score, and return feedback.
    return unfinished_response()


if __name__ == "__main__":
    app.run(debug=True, port=5000)

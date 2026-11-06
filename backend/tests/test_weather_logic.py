"""Guiding tests: these intentionally fail until builders implement the TODOs."""

import unittest

from backend.sample_weather import SAMPLE_WEATHER
from backend.weather_logic import (
    calculate_average_temperature,
    find_coldest_day,
    find_hottest_day,
    find_wettest_day,
    umbrella_recommendation,
)


class ForecastAnalysisTests(unittest.TestCase):
    def setUp(self):
        self.forecast = SAMPLE_WEATHER["Kigali"]["forecast"]

    def test_finds_hottest_day(self):
        self.assertEqual(find_hottest_day(self.forecast)["date"], "2026-10-19")

    def test_finds_coldest_day(self):
        self.assertEqual(find_coldest_day(self.forecast)["date"], "2026-10-18")

    def test_calculates_average_maximum_temperature(self):
        self.assertAlmostEqual(calculate_average_temperature(self.forecast), 27.0)

    def test_ignores_missing_precipitation(self):
        forecast = [{"date": "a", "precipitation_probability": None}, {"date": "b", "precipitation_probability": 60}]
        self.assertEqual(find_wettest_day(forecast)["date"], "b")


class UmbrellaTests(unittest.TestCase):
    def test_recommends_umbrella_at_or_above_threshold(self):
        result = umbrella_recommendation(40)
        self.assertTrue(result["bring_umbrella"])

    def test_does_not_recommend_umbrella_below_threshold(self):
        result = umbrella_recommendation(39)
        self.assertFalse(result["bring_umbrella"])

    def test_handles_missing_probability(self):
        result = umbrella_recommendation(None)
        self.assertIn("unknown", result["recommendation"].lower())

if __name__ == "__main__":
    unittest.main()

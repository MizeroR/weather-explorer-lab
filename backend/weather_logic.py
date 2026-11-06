"""Builder-owned weather calculations.

Use sample_weather.SAMPLE_WEATHER while developing. Keep these functions free
from HTTP requests so they are easy to test with small dictionaries.
"""

DEFAULT_UMBRELLA_THRESHOLD = 40


def _unfinished(task):
    raise NotImplementedError(f"Builder task: {task}")


# TODO 1: backend/weather_logic.py -> find_hottest_day
# Loop through forecast and return the complete day dictionary whose
# temperature_max is greatest. Expected result: Kigali's result has date
# "2026-10-19". Decide what an empty list should do, then run the focused test.
def find_hottest_day(forecast):
    """Return the forecast day with the largest temperature_max value."""
    return _unfinished("loop through forecast and find the hottest day")


# TODO 2: backend/weather_logic.py -> find_coldest_day
# Return the day dictionary with the smallest temperature_min. Expected result:
# Kigali's result has date "2026-10-18". Use the same empty-list decision as the first task.
def find_coldest_day(forecast):
    """Return the forecast day with the smallest temperature_min value."""
    return _unfinished("loop through forecast and find the coldest day")


# TODO 3: backend/weather_logic.py -> calculate_average_temperature
# Read each temperature_max, skip missing values, add the remaining numbers, and
# divide by their count. Expected result: Kigali returns 27.0.
def calculate_average_temperature(forecast):
    """Return the average of available daily maximum temperatures."""
    return _unfinished("add available temperatures and divide by their count")


# TODO 4: backend/weather_logic.py -> find_wettest_day
# Compare only precipitation_probability values that are not None and return
# that day's complete dictionary. Expected result: Kigali returns 65% on
# "2026-10-20"; an empty usable set needs a clear result.
def find_wettest_day(forecast):
    """Return the day with the highest available precipitation probability."""
    return _unfinished("ignore missing probabilities and find the largest value")


# TODO 5: backend/weather_logic.py -> umbrella_recommendation
# Validate probability and threshold, then compare them using the 40% default.
# Expected result: 40 returns bring_umbrella=True, 39 returns False, and None
# produces a recommendation containing "unknown". Return a recommendation and
# explanation; missing data should never be guessed.
def umbrella_recommendation(probability, threshold=DEFAULT_UMBRELLA_THRESHOLD):
    """Return a recommendation and explanation based on a configurable percentage."""
    return _unfinished("validate probability, compare it with threshold, and explain")

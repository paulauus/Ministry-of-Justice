"""
This file includes tests for the file test_3.py.
"""

from test_3 import sum_current_time

def test_sum_current_time():
    """Tests the function returns the correct number."""
    assert sum_current_time("01:23:45") == 15


def test_sum_current_time_bad_input():
    """Tests bad input returns error message."""
    assert sum_current_time("1:2:3") == "Error: Expects data in the format HH:MM:SS."
    assert sum_current_time(
        "00:01") == "Error: Expects data in the format HH:MM:SS."
    assert sum_current_time(
        "121314") == "Error: Expects data in the format HH:MM:SS."
    assert sum_current_time(
        "1:23:456") == "Error: Expects data in the format HH:MM:SS."

def test_sum_current_time_letters():
    """Tests letters return error message."""
    assert sum_current_time(
        "aa:bb:cc") == "Error: Expects data in the format HH:MM:SS."
    assert sum_current_time(
        "12:34:ab") == "Error: Expects data in the format HH:MM:SS."

def test_sum_current_time_bad_time():
    """Tests the time given is valid."""
    assert sum_current_time("24:99:80") == "Error: Not a valid time."
    assert sum_current_time("00:00:60") == "Error: Not a valid time."

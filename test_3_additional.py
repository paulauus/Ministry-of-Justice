"""
This file includes tests for the file test_3.py.
"""

from test_3 import sum_current_time

def test_sum_current_time():
    """Tests the function returns the correct number."""
    assert sum_current_time("01:23:45") == 15


def test_sum_current_time_bad_input():
    """Tests bad input returns error message."""
    assert sum_current_time("1:2:3") == "Error: Expects data in the format HH:MM:SS"

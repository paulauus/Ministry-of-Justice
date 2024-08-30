"""
This file includes additional tests for test_1.py.
"""

from test_1 import is_log_line, get_dict


def test_valid_log_line():
    """Tests valid log line is True."""
    line = "03/11/21 08:51:01 INFO    :.main: Using log level 511"

    result = is_log_line(line)

    assert result is True


def test_invalid_log_line():
    """Tests invalid log line is False."""
    line = "INFO    :.main: Missing timestamp in this log line"

    result = is_log_line(line)

    assert result is False


def test_get_dict():
    """Tests function handles time, log and message."""
    line = "04/11/21 10:55:21 WARNING :This is a test message"
    expected = {
        "timestamp": "04/11/21 10:55:21",
        "log_level": "WARNING",
        "message": ":This is a test message"
    }
    actual = get_dict(line)
    assert expected == actual

def test_get_dict_no_message():
    """Tests function handles no message."""
    line = "04/11/21 10:55:21 WARNING"
    expected = {
        "timestamp": "04/11/21 10:55:21",
        "log_level": "WARNING",
        "message": ""
    }
    actual = get_dict(line)
    assert expected == actual

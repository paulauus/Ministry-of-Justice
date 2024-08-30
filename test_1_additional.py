from test_1 import is_log_line


def test_valid_log_line():
    # Valid log line example
    line = "03/11/21 08:51:01 INFO    :.main: Using log level 511"

    # Call the function with the valid log line
    result = is_log_line(line)

    # Assert that the result is True
    assert result is True


def test_invalid_log_line():
    line = "INFO    :.main: Missing timestamp in this log line"

    # Call the function with the invalid log line
    result = is_log_line(line)

    # Assert that the result is False
    assert result == False

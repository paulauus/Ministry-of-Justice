"""
Task 3:

A function that adds all the individual numbers at the current time.
"""

# The below function doesn't work correctly. It should sum all the numbers at the
# current time. For example, 01:02:03 should return 6. Improve and fix the function,
# and write unit test(s) for it. Use any testing framework you're familiar with.


# [TODO]: fix the function
def sum_current_time(time_str: str) -> int:
    """Expects data in the format HH:MM:SS"""
    if len(time_str) != 8:
        return "Error: Expects data in the format HH:MM:SS"
    parts = time_str.split(":")
    if len(parts) != 3:
        return "Error: Expects data in the format HH:MM:SS"
    hours = parts[0]
    minutes = parts[1]
    seconds = parts[2]
    if len(hours) != 2 or len(minutes) != 2 or len(seconds) != 2:
        return "Error: Expects data in the format HH:MM:SS"
    try:
        digits = [int(digit) for digit in hours] + [int(digit) for digit in minutes] + [int(digit) for digit in seconds]
    except ValueError:
        return "Error: Expects data in the format HH:MM:SS"
    sum_of_digits = 0
    for num in digits:
        sum_of_digits += num
    return sum_of_digits
# ValueError

if __name__ == "__main__":

    print(sum_current_time("01:23:45"))
    print(sum_current_time("01:ab:45"))
    print(sum_current_time("aa:bb:cc"))

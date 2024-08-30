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

    # Check the input is in correct format
    if len(time_str) != 8 or time_str[2] != ':' or time_str[5] != ':':
        return "Error: Expects data in the format HH:MM:SS"

    parts = time_str.split(":")
    # Check that the legth of each part is 2
    if any(len(part) != 2 for part in parts):
        return "Error: Each part of the time string must be exactly 2 digits long"

    try:
        sum_of_digits = sum(int(digit) for part in parts for digit in part)
    except ValueError:
        return "Error: Expects data in the format HH:MM:SS"

    return sum_of_digits

if __name__ == "__main__":

    print(sum_current_time("01:23:45"))
    print(sum_current_time("01:ab:45"))
    print(sum_current_time("aa:bb:cc"))
    print(sum_current_time("1:24:234"))
    

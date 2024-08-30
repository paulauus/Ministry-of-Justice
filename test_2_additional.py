"""
This file includes additional tests for test_2.py.
"""

from test_2 import get_nearest_courts, find_nearest_court


def test_fetch_nearest_courts(mock_requests_get):
    # Define a sample JSON response that the API might return
    response = {}

    # Set up the mock to return a response with our sample JSON data
    mock_requests_get.return_value.json.return_value = response

    postcode = 'SW1A 1AA'
    result = get_nearest_courts(postcode)

    # Check that requests.get was called with the correct URL
    expected_url = f"https://www.find-court-tribunal.service.gov.uk/search/results.json?postcode={postcode}"
    mock_requests_get.assert_called_once_with(expected_url)
    assert result == response


def test_closest_court_found():
    """Tests that the nearest court of correct type is output."""
    courts_data = [
        {"name": "Court A", "types": [
            "Criminal", "Civil"], "dx_number": "DX 12345", "distance": 2.5},
        {"name": "Court B", "types": ["Family"], "distance": 1.0},
        {"name": "Court C", "types": ["Criminal"], "distance": 3.0},
    ]

    expected_result = {
        "name": "Court A",
        "dx_number": "DX 12345",
        "distance": 2.5
    }

    result = find_nearest_court(courts_data, "Criminal")
    assert result == expected_result


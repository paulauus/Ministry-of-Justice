"""
This file includes additional tests for test_2.py.
"""

from test_2 import get_nearest_courts


def test_fetch_nearest_courts(mock_requests_get):
    # Define a sample JSON response that the API might return
    response = {
        "courts": [
            {"name": "Court 1", "address": "Address 1"},
            {"name": "Court 2", "address": "Address 2"}
        ]
    }

    # Set up the mock to return a response with our sample JSON data
    mock_requests_get.return_value.json.return_value = response

    postcode = 'SW1A 1AA'
    result = get_nearest_courts(postcode)

    # Check that requests.get was called with the correct URL
    expected_url = f"https://www.find-court-tribunal.service.gov.uk/search/results.json?postcode={postcode}"
    mock_requests_get.assert_called_once_with(expected_url)

    assert result == response



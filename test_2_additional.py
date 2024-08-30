"""
This file includes additional tests for test_2.py.
"""

from unittest.mock import patch
import pandas as pd
from test_2 import get_courts_at_postcode, find_nearest_court, find_court_for_each_person


def test_get_courts_at_postcode(mock_requests_get):
    """Test the nearest airports are returned in the correct dict format."""
    # Define a sample JSON response
    response = {}

    # Set up the mock to return a response with the sample JSON data
    mock_requests_get.return_value.json.return_value = response

    postcode = 'SW1A 1AA'
    result = get_courts_at_postcode(postcode)

    # Check that requests.get was called with the correct URL
    expected_url = f"https://www.find-court-tribunal.service.gov.uk/search/results.json?postcode={postcode}"
    mock_requests_get.assert_called_once_with(expected_url, timeout=10)
    assert result == response


def test_find_nearest_court():
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


mock_people_df = pd.DataFrame([
    {
        "person_name": "John Doe",
        "home_postcode": "SW1A 1AA",
        "looking_for_court_type": "Criminal"
    },
    {
        "person_name": "Jane Smith",
        "home_postcode": "E1 6AN",
        "looking_for_court_type": "Family"
    }
])

mock_courts_data = [
    {"name": "Court A", "types": ["Criminal", "Civil"],
        "dx_number": "DX 12345", "distance": 2.5},
    {"name": "Court B", "types": ["Family"],
        "dx_number": "DX 67890", "distance": 1.0}
]

mock_nearest_court_criminal = {
    "name": "Court A",
    "dx_number": "DX 12345",
    "distance": 2.5
}

mock_nearest_court_family = {
    "name": "Court B",
    "dx_number": "DX 67890",
    "distance": 1.0
}


@patch('test_2.get_courts_at_postcode')
@patch('test_2.find_nearest_court')
def test_find_court_for_each_person(mock_find_nearest_desired_court, mock_fetch_nearest_courts):
    """Test test correct courts are found for the people on the list."""
    mock_fetch_nearest_courts.side_effect = [
        mock_courts_data, mock_courts_data]
    mock_find_nearest_desired_court.side_effect = [
        mock_nearest_court_criminal, mock_nearest_court_family]

    expected_result = [
        {
            "name": "John Doe",
            "home_postcode": "SW1A 1AA",
            "desired_court_type": "Criminal",
            "nearest_court": "Court A",
            "dx_number": "DX 12345",
            "distance": 2.5
        },
        {
            "name": "Jane Smith",
            "home_postcode": "E1 6AN",
            "desired_court_type": "Family",
            "nearest_court": "Court B",
            "dx_number": "DX 67890",
            "distance": 1.0
        }
    ]

    result = find_court_for_each_person(mock_people_df)
    assert result == expected_result

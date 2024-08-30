"""
Test 2:

This file includes three functions used to find the closest court
of the correct type for each person in the people.csv file.
"""

import requests
import pandas as pd

# A team of analysts wish to discover how far people are travelling to their nearest
# desired court. We have provided you with a small test dataset so you can find out if
# it is possible to give the analysts the data they need to do this. The data is in
# `people.csv` and contains the following columns:
# - person_name
# - home_postcode
# - looking_for_court_type

# The courts and tribunals finder API returns a list of the 10 nearest courts to a
# given postcode. The output is an array of objects in JSON format. The API is
# accessed by including the postcode of interest in a URL. For example, accessing
# https://www.find-court-tribunal.service.gov.uk/search/results.json?postcode=E144PU gives
# the 10 nearest courts to the postcode E14 4PU. Visit the link to see an example of
# the output.

# Below is the first element of the JSON array from the above API call. We only want the
# following keys from the json:
# - name
# - dx_number
# - distance
# dx_number is not always returned and the "types" field can be empty.

"""
[
    {
        "name":"East London Family Court",
        "lat":51.5063346382936,
        "lon":-0.0261344650867725,
        "number":null,
        "cci_code":null,
        "magistrate_code":null,
        "slug":"east-london-family-court",
        "types":["Family Court"],
        "areas_of_law":[{"name":"Adoption","external_link":"https://www.gov.uk/child-adoption","display_url":null,"external_link_desc":"Information about adopting a child","display_name":null,"display_external_link":"https://www.gov.uk/child-adoption/applying-for-an-adoption-court-order"},
                        {"name":"Children","external_link":null,"display_url":null,"external_link_desc":null,"display_name":"Childcare arrangements if you separate from your partner","display_external_link":"https://www.gov.uk/looking-after-children-divorce"},
                        {"name":"Divorce","external_link":"https://www.gov.uk/divorce","display_url":null,"external_link_desc":"Information about getting a divorce","display_name":null,"display_external_link":null},
                        {"name":"Domestic violence","external_link":null,"display_url":null,"external_link_desc":null,"display_name":"Domestic abuse","display_external_link":"https://www.gov.uk/injunction-domestic-violence"},
                        {"name":"FGM","external_link":"https://www.gov.uk/government/collections/female-genital-mutilation","display_url":null,"external_link_desc":null,"display_name":"Female Genital Mutilation","display_external_link":null},
                        {"name":"Forced marriage","external_link":"https://www.gov.uk/apply-forced-marriage-protection-order","display_url":null,"external_link_desc":"Information about forced marriage protection orders","display_name":null,"display_external_link":null}],
        "areas_of_law_spoe":["Children"],
        "displayed":true,
        "hide_aols":false,
        "dx_number":"316201 Docklands 3",
        "distance":0.21,
        "addresses":[{"address_lines":["East London Family Court","6th and 7th Floor, 11 Westferry Circus",
                                       "(Entrance in Columbus Courtyard)"],
                      "postcode":"E14 4HD",
                      "town":"London",
                      "type":"Visit or contact us",
                      "county":"Greater London",
                      "description":null,
                      "fields_of_law":null}]
    },
    ...
]
"""

# Use this API and the data in people.csv to determine how far each person's nearest
# desired court is. Generate an output (of whatever format you feel is appropriate)
# showing, for each person:
# - name
# - type of court desired
# - home postcode
# - nearest court of the right type
# - the dx_number (if available) of the nearest court of the right type
# - the distance to the nearest court of the right type


def get_courts_at_postcode(postcode) -> list[dict]:
    """Gets the nearest courts to a postcode."""
    url = f"https://www.find-court-tribunal.service.gov.uk/search/results.json?postcode={postcode}"
    response = requests.get(url, timeout=10)

    return response.json()


def find_nearest_court(courts, court_type) -> dict:
    """Finds the closest court of the required type to a given postcode."""
    nearest_court = None
    min_distance = float("inf")

    for court in courts:
        if court_type in court["types"]:
            if court["distance"] < min_distance:  # If the court is closer
                nearest_court = {
                    "name": court['name'],
                    "dx_number": court.get('dx_number', None),
                    "distance": court['distance']
                }
                min_distance = court["distance"]  # Update min distance

    return nearest_court


def find_court_for_each_person(people) -> list[dict]:
    """Finds the closes required court for each person in the data."""
    results = []

    for _, row in people.iterrows():
        name = row['person_name']
        home_postcode = row['home_postcode']
        desired_court_type = row['looking_for_court_type']

        courts_data = get_courts_at_postcode(home_postcode)
        nearest_court = find_nearest_court(
            courts_data, desired_court_type)

        if nearest_court:
            results.append({
                "name": name,
                "home_postcode": home_postcode,
                "desired_court_type": desired_court_type,
                "nearest_court": nearest_court['name'],
                "dx_number": nearest_court['dx_number'],
                "distance": nearest_court['distance']
            })
        else:
            results.append({
                "name": name,
                "home_postcode": home_postcode,
                "desired_court_type": desired_court_type,
                "nearest_court": "No court found",
                "dx_number": None,
                "distance": None
            })

    return results


if __name__ == "__main__":
    # [TODO]: write your answer here

    # Load the csv data
    people_df = pd.read_csv("people.csv")

    # Find the nearest court to each person and extract the data
    courts_results = find_court_for_each_person(people_df)

    # Convert the results to a DataFrame
    results_df = pd.DataFrame(courts_results)
    print(results_df)

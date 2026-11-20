from Chapter_11_functions.city_functions import city_country

"""
    Functions that test the city_country function in pytest
"""


def test_city_country():
    """Does this yield the format City, Country?"""

    formatted_city_country = city_country("santiago", "chile")
    assert formatted_city_country == "Santiago, Chile"


def test_city_country_population():
    """Does this yield format City, Country - population xxx"""

    formatted_city_country_population = city_country(
        "santiago", "chile", 5000000
    )

    # harcoded expected result of city_country function
    valid_output = "Santiago, Chile - population 5000000"

    assert formatted_city_country_population == valid_output

"""
Goal: Main f(x) to pass into test F(x)'s
"""


def city_country(city, country, population=""):
    """A function that returns a string for city country"""

    if population == "":
        city_country_str = f"{city.title()}, {country.title()}"

    else:
        city_country_str = f"{city.title()}, {country.title()} "
        city_country_str = city_country_str + f"- population {population}"

    return city_country_str

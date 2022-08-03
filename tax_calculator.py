import pandas as pd
import re


def get_year_prompt() -> str:
    """
    Prompts user for year to calculate the tax for.

    Returns:
        str: year (e.g.2020-2021)

    """
    year = input("Please enter the income year (eg: 2020-2021): ")
    year = year.strip()

    # Keep prompting the user for input until a valid year is entered
    if not re.fullmatch(r'\d{4}-\d{4}', year):
        print("Invalid Input. Kindly try again.")
        return get_year_prompt()

    # Check whether the tax year is in the database and quit if not
    if year not in pd.ExcelFile('tax_rates.xlsx').sheet_names:
        print("Tax information not available for the given year.")
        exit()

    return year

import pandas as pd
import re
from decimal import Decimal


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


def get_income_prompt() -> float:
    """
    Prompts user for income to calculate tax for.

        Returns:
            float : income (e.g.23456.45)

    """
    try:
        income = input("Please enter the income: ")
        income = float(income.strip())
    except ValueError:
        print("Invalid Input. Kindly try again.")
        return get_income_prompt()
    return income


def calculate_tax(year: str, income: float) -> float:
    """
    Calculates tax for the given income and year.

    Args:
        year (str): year (e.g.2020-2021)
        income (float): income (e.g.23456.45)

    Returns:
        float: tax (e.g.2345.00)

    """
    # Read the tax brackets from the excel file
    taxes = pd.read_excel('tax_rates.xlsx', sheet_name=year)

    # Find the tax bracket for the given income
    tax_bracket = taxes[(taxes['Lower_Limit'] <= income) & (taxes['Upper_Limit'] >= income)].iloc[0]

    # Calculate the tax for the given income
    tax = tax_bracket['Fixed_Tax'] + (tax_bracket['Tax_Rate']/100.0) * (income - max(0, tax_bracket['Lower_Limit']-1))

    # Round the tax to the nearest cent
    tax = float(Decimal(tax).quantize(Decimal('0.01')))
    return tax


def main():
    """
    Main function dictating the flow of the program.
    """
    year = get_year_prompt()
    income = get_income_prompt()
    tax = calculate_tax(year, income)
    print(f"The estimated tax on your given income is: ${tax:,.2f}")


if __name__ == "__main__":
    main()

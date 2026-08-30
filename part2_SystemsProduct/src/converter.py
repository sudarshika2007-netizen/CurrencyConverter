import json
import os


def load_rates(filename="rates.json"):
    """Load exchange rates from rates.json."""

    if not os.path.exists(filename):
        raise FileNotFoundError("rates.json file was not found.")

    with open(filename, "r") as file:
        rates = json.load(file)

    return rates


def convert_currency(amount, from_currency, to_currency, rates):
    """Convert money from one currency to another."""

    if amount < 0:
        raise ValueError("Amount cannot be negative.")

    from_currency = from_currency.upper()
    to_currency = to_currency.upper()

    if from_currency not in rates:
        raise ValueError(f"Unsupported currency code: {from_currency}")

    if to_currency not in rates:
        raise ValueError(f"Unsupported currency code: {to_currency}")

    # Convert source currency to USD
    amount_in_usd = amount / rates[from_currency]

    # Convert USD to target currency
    converted_amount = amount_in_usd * rates[to_currency]

    return converted_amount

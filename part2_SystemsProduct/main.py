import argparse

from src.converter import load_rates, convert_currency
from src.logger import setup_logger


def main():
    logger = setup_logger()

    parser = argparse.ArgumentParser(
        description="Currency Converter"
    )

    parser.add_argument(
        "--from",
        dest="from_currency",
        required=True,
        help="Currency to convert from"
    )

    parser.add_argument(
        "--to",
        dest="to_currency",
        required=True,
        help="Currency to convert to"
    )

    parser.add_argument(
        "--amount",
        required=True,
        help="Amount to convert"
    )

    args = parser.parse_args()

    try:
        try:
            amount = float(args.amount)
        except ValueError:
            raise ValueError("Amount must be a number.")

        rates = load_rates()

        result = convert_currency(
            amount,
            args.from_currency,
            args.to_currency,
            rates
        )

        print(
            f"{amount:.2f} {args.from_currency.upper()} = "
            f"{result:.2f} {args.to_currency.upper()}"
        )

        logger.info(
            "Successful conversion: %.2f %s to %.2f %s",
            amount,
            args.from_currency.upper(),
            result,
            args.to_currency.upper()
        )

    except (ValueError, FileNotFoundError) as error:
        print(f"Error: {error}")
        logger.error("Conversion failed: %s", error)

    except Exception as error:
        print("Error: Something went wrong. Please try again.")
        logger.error("Unexpected error: %s", error)


if __name__ == "__main__":
    main()

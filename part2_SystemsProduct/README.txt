CURRENCY CONVERTER - PROGRAMMING SYSTEMS PRODUCT

1. PROJECT DESCRIPTION

This project is a command-line currency converter developed using Python.

The system converts an amount from one supported currency to another
using exchange rates stored in an external JSON configuration file.

The project includes:
- Currency conversion
- External configuration using rates.json
- Command-Line Interface (CLI)
- Error handling
- Logging
- Automated unit tests
- Documentation


2. REQUIREMENTS

Python 3.x is required.

No external Python packages are required.


3. PROJECT STRUCTURE

Part2_SystemsProduct/
|
|-- src/
|   |-- converter.py
|   |-- logger.py
|
|-- tests/
|   |-- test_converter.py
|
|-- main.py
|-- rates.json
|-- requirements.txt
|-- README.txt
|-- app.log


4. HOW TO RUN

Open Command Prompt inside the Part2_SystemsProduct folder.

Run the program using:

python main.py --from USD --to INR --amount 100


5. COMMAND-LINE ARGUMENTS

--from

Specifies the currency to convert from.

Example:

--from USD


--to

Specifies the currency to convert to.

Example:

--to INR


--amount

Specifies the amount to convert.

Example:

--amount 100


6. USAGE EXAMPLES

Example 1:

python main.py --from USD --to INR --amount 100

Output:

100.00 USD = 9524.00 INR


Example 2:

python main.py --from INR --to USD --amount 9524

Output:

9524.00 INR = 100.00 USD


Example 3:

python main.py --from USD --to EUR --amount 100

Output:

100.00 USD = 85.00 EUR


7. SUPPORTED CURRENCIES

The supported currencies are stored in rates.json.

Currently supported currencies include:

USD
INR
EUR
GBP
JPY
AUD
CAD


8. CONFIGURATION

Exchange rates are stored in the external file:

rates.json

The rates are relative to USD.

For example:

USD = 1.0
INR = 95.24
EUR = 0.85

The rates can be updated by editing rates.json.


9. ERROR HANDLING

The program handles invalid input without displaying raw Python
tracebacks.

Examples of handled errors include:

- Negative amounts
- Non-numeric amounts
- Unsupported currency codes
- Missing rates.json file

Example:

python main.py --from USD --to INR --amount -50

Output:

Error: Amount cannot be negative.


10. LOGGING

The application records successful conversions and errors in:

app.log

Each log entry contains the date, time, log level, and description
of the operation.


11. TESTING

Automated unit tests are provided in:

tests/test_converter.py

Run the tests using:

python -m unittest discover -s tests -v

The tests cover:

- USD to INR conversion
- INR to USD conversion
- USD to EUR conversion
- Zero amount
- Negative amount
- Unsupported source currency
- Unsupported target currency


12. CONCLUSION

This project demonstrates the difference between a simple program
and a programming systems product.

The Part 2 implementation improves the original converter by adding
external configuration, a command-line interface, error handling,
logging, automated testing, and documentation.

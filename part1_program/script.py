# Part 1: Simple Currency Converter

print("===== Currency Converter =====")
print("Fixed Exchange Rate: 1 USD = 95.24 INR")
print()

# Fixed exchange rate
INR_TO_USD = 95.24

# Get input from the user
amount = float(input("Enter the amount in INR: "))

# Convert INR to USD
usd_amount = amount / INR_TO_USD

# Display the result
print()
print(f"Original Amount: ₹{amount:.2f}")
print(f"Converted Amount: ${usd_amount:.2f}")

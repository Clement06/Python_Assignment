def calculate_emis(principal_amount, monthly_emi):
    total_emis = principal_amount / monthly_emi
    return round(total_emis)


# Given variables
principal_amount = 1000000  # Rs. 10,00,000.00
monthly_emi = 15000  # Rs. 15,000.00
annual_interest_rate = 12  # 12% per year

# Convert annual interest rate to monthly interest rate
monthly_interest_rate = annual_interest_rate / 12 / 100

# Calculate total EMIs needed to complete the loan
total_emis = calculate_emis(principal_amount, monthly_emi)

print(f"The customer needs to pay {total_emis} EMIs to complete the loan.")

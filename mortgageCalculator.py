principal = int(input("ENTER OF PRINCIPLE: "))

annual_interest_rate = float(input("ENTER INTEREST RATE: "))

loan_terms = int(input("ENTER LOAN TERMS: "))

Months_in_year = 12

monthly_interest_rate = annual_interest_rate / Months_in_year

monthly_interest_rate = monthly_interest_rate / 100

loan_terms_months = loan_terms * Months_in_year

monthly_payment = (principal * monthly_interest_rate) // (1 - (1 + monthly_interest_rate)**(-loan_terms_months))

print(f"${monthly_payment}")
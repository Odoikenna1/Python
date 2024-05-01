#a = p(1 + r)n
one = 1
annual_rate_Of_return = 7 / 100 
number_Of_years = int(input("Enter number of years: "))
principal = int(input("Enter your principal amount: "))

amount_on_deposit = principal * (one + annual_rate_Of_return) * number_Of_years

print(f"Your return on investment at the nth year is {amount_on_deposit}")
amount = int(input("enter amount: "))

numberOfYears = int(input("enter number of years: "))

RATE = 20

PERCENTAGE = 100

RATEPERCENT = RATE / PERCENTAGE



for i in range(1,numberOfYears +1):
		interest = amount * RATEPERCENT
		amount = interest + amount
		print(f"interest for year {i} is: {interest:.2f}\nUpdated Cost is: {amount:.2f}\n")


	



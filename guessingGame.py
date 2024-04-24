#number guessing game

CORRECTNUMBER = 9

for n in range(3):
	userInput = int(input("Enter a number between 1 - 10 (You have 3 chances only): "))
	if userInput == DEFAULT:
		print("You won",)
		break
	if userInput != DEFAULT:
		print("Failed, Try again")





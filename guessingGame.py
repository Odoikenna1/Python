#number guessing game

import random

LUCKY_NUMBER = random.randrange(1,10)

userInput = 0

while userInput != LUCKY_NUMBER:
	userInput = int(input("Enter a number between 1 - 10 (You have 3 chances only): "))
	if userInput == LUCKY_NUMBER:
		print("You won")
		break
	else:
		print("Failed, Try again")
	





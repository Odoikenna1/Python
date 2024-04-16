#collect multiple inputs
#use split function to separate them
#Find even and odd numbers from user input

items = list(map(int, input("Enter multpile values on this line: ").split()))

for num in items:

	if num % 2 == 0:

		print(f"{num} is an even number")

	else:

		print(f"{num} is an odd number")
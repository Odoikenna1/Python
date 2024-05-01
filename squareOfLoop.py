def squareOfLoop(number):
	return i ** 2

for i in range(1,11):
	print(squareOfLoop(i))




def summationx(numbers, x):
	total = 0
	for i in numbers:
		total += i
	return total + x

print(summationx([1,2,3,4,34,12], 50))
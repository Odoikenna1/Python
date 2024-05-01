PASS_MARK = 45
number_failed = 0
number_passed = 0
score = 0
score_counter = 0

for number in range(15):
	score = int(input("Enter scores: "))
	score_counter += 1

	if score > PASS_MARK:
		 number_passed += 1
	if score < PASS_MARK:
		 number_failed += 1

print(f"\nNumber of scores entered: {score_counter}")
print(f"Number of students passed: {number_passed}")
print(f"Number of students failed: {number_failed}")






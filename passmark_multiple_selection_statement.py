#A program that determines your success in a course based on the user input
#the pass mark is 45

#Score Grading System

#score between 80 - 100 A
#score between 65 - 79 B
#score between 50 - 64 C
#score between 40 - 49 D
#score equal to below 48

studentGrade = int(input("ENTER GRADE: "))

if studentGrade > 100:
	print(f"Your score is {studentGrade}\nYou are a CRIMINAL!!\nYou should be arrested!")

elif studentGrade >= 50 and studentGrade <= 64:
	print(f"Your score is {studentGrade}\nYour grade is C")

elif studentGrade >= 40 and studentGrade <= 49:
	print(f"Your score is {studentGrade}\nYour grade is D")

elif studentGrade <=48:
	print(f"Your score is {studentGrade}\nYou Failed")

elif studentGrade > 100:
	print(f"Your score is {studentGrade}\nYou are a CRIMINAL!!\nYou should be arrested!")



else:
	print("NO SCORE ENTERED")


print("Enter two integers, and I will tell you the relationships they satisfy")

user_input = int(input("Enter two numbers: "))
num1 = user_input

user_input2 = int(input("Enter two numbers: "))
num2 = user_input2

print(num1, num2)
if num1 == num2:
    print(f"{num1 } is equal to { num2}")
elif num1 < num2:
    print(f"{num1 } is less than { num2}")
elif num1 > num2:
    print(f"{num1 } is grater than { num2}")
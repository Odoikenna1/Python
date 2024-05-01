program_isActive = 0
alternative_value1 = 1
alternative_value2 = 2
passes = 0
failures = 0

while program_isActive < 10:
    user_input =int(input("Enter a number: "))
    if user_input == alternative_value1:
        passes+=1
    if user_input == alternative_value2:
        failures+=1
    program_isActive+=1
print(f"The number of passes is: { passes}\nThe number of failures: { failures}")
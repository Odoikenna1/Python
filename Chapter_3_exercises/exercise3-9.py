user_input = 12321
temp = str(user_input)

for index in temp:
    remainder = user_input % 10
    user_input = user_input // 10
    print(str(remainder), end=" ")
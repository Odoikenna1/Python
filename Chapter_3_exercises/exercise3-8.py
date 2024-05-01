sum = 0
input_count = 1
product = 1
for i in range(4):
    user_input = int(input("Enter a number: "))
    sum += user_input
    average = sum / input_count
    product *= user_input
    input_count+=1
    
print(f"\nsum is: {sum}\naverage is: {average}\nproduct is {product}")
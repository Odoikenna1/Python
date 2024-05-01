user_input = input("What is your problem? ")
user_response = user_input

get_more_data = input("Have you had this problem before? ")
positive_response = "yes"
negative_response = "no"

result1 = get_more_data.lower() == positive_response.lower()
result2 = get_more_data.lower() == negative_response.lower()

if result1:
    print("Well you have again.\nI would make some prescriptions but unfortunately I can't.\nCheck back later.")
else:
    print("Well you have it now.")
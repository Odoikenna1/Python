price = int(input("\nENTER PRICE: "))

discount = float(input("\nENTER DISCOUNT: "))

discount = discount / 100

discounted_price = price * discount

print(f"\nOriginal price is: {price}\nThe discounted price is {discounted_price}")


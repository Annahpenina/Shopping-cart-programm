foods = []
prices = []
total = 0

# While loop
while True:
    food = input("Enter food to buy or press 'q' to quit: ")
    if food.lower() == 'q':
        break
    else:
        try:
            price = float(input(f"Enter the price of {food}: R"))
            foods.append(food)
            prices.append(price)
        except ValueError:
            print("Please enter a valid number for the price.")


print("\n----- YOUR CART -----")
for i in range(len(foods)):
    print(f"{foods[i]} - R{prices[i]:.2f}")
    total += prices[i]

print(f"\nYour total is: R{total:.2f}")

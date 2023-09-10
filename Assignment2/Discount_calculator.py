# Define the unit price and discount percentages
unit_price = 5
discount_after_30 = 30
discount_after_50 = 50
discount_percentage_after30 = 10
discount_percentage_after50 = 15

# Input quantity from the user
quantity = int(input("Enter the quantity: "))

# Calculate the price
if quantity <= 0:
    print("Invalid quantity. Quantity should be a positive integer.")
else:
    if quantity > discount_after_50:
        price = quantity * unit_price * (1 - discount_percentage_after50 / 100)
    elif quantity > discount_after_30:
        price = quantity * unit_price * (1 - discount_percentage_after30 / 100)
    else:
        price = quantity * unit_price

    # Display the calculated price
    print(f"Total price for {quantity} items: Rs {price:.2f}")

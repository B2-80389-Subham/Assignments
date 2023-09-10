num_calls = int(input("Enter the number of calls: "))
bill = 200

# Calculate the bill based on the rules
if num_calls > 100:
    # Calculate the cost for the first 50 calls beyond 100
    bill += (min(num_calls, 150) - 100) * 0.60

    if num_calls > 150:
        # Calculate the cost for the next 50 calls beyond 150
        bill += (min(num_calls, 200) - 150) * 0.50

        if num_calls > 200:
            # Calculate the cost for calls beyond 200
            bill += (num_calls - 200) * 0.40

print(f"Your monthly telephone bill is Rs. {bill:.2f}")

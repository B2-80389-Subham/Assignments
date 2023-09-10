# Input a 4-digit number
number = int(input("Enter a 4-digit number: "))

# Extract individual digits
digit_1 = number // 1000
digit_2 = (number // 100) % 10
digit_3 = (number // 10) % 10
digit_4 = number % 10

# Display face values
print(f"Face values of each digit: {digit_1} {digit_2} {digit_3} {digit_4}")

# Display place values
place_value_1 = digit_1 * 1000
place_value_2 = digit_2 * 100
place_value_3 = digit_3 * 10
place_value_4 = digit_4 * 1

print(f"Place values of each digit: {place_value_1} + {place_value_2} + {place_value_3} + {place_value_4}")

# Display the number in reverse order with changed decimal place values
reversed_number = digit_4 * 1000 + digit_3 * 100 + digit_2 * 10 + digit_1 * 1
print(f"Number in reverse order with changed decimal place values: {reversed_number}")

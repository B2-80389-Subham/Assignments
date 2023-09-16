Str1 = "Python83737@#8496"
digit_sum = 0
digit_count = 0
for char in Str1:
    if char.isdigit():  # Check if the character is a digit
        digit_sum += int(char)  # Add the digit to the sum
        digit_count += 1  # Increment the digit count
if digit_count > 0:
    digit_average = digit_sum / digit_count
else:
    digit_average = 0  # Avoid division by zero if there are no digits
print("Sum of digits:", digit_sum)
print("Average of digits:", digit_average)

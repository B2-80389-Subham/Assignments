def find_maximum(num1, num2, num3):
    # Compare the three numbers and return the maximum
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))
num3 = int(input("Enter the 3rd number: "))
maximum = find_maximum(num1, num2, num3)
print(f"The maximum of {num1}, {num2}, and {num3} is: {maximum}")

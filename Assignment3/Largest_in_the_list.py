empty_list = []
n = int(input("Enter the number of values: "))
for i in range(n):
    value = int(input(f"Enter value {i + 1}: "))
    empty_list.append(value)

max_value = empty_list[0]

# maximum value
for num in empty_list:
    if num > max_value:
        max_value = num
print(f"The largest number in the list is: {max_value}")

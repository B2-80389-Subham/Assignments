input_list = input("Enter a list of elements separated by spaces: ").split()
count = 0
for item in input_list:
    if item.startswith("(") and item.endswith(")"):
        break
    count += 1
print(f"The number of elements before a tuple is: {count}")

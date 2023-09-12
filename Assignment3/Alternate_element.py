user_list = input("Enter a list of elements separated by spaces: ").split()
print("Alternate elements of the list:")
for i in range(0, len(user_list), 2):
    print(user_list[i])

original_list = [('Python', 88), ('ML', 90), ('Rprogramming', 97), ('DBMS', 82)]
sorted_list = sorted(original_list, key=lambda x: x[1])
print("Sorting the List of Tuples:")
print(sorted_list)

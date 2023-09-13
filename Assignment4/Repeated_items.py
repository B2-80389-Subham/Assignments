input_data = tuple(input("Enter a tuple of values (comma-separated): ").split(','))
repetitions = input("Enter the value to find repetitions: ")
count = input_data.count(repetitions)
# repeating value checking
if count > 1:
    print(f"The value '{repetitions}' repeats {count} times in the tuple.")
elif count == 1:
    print(f"The value '{repetitions}' appears once in the tuple.")
else:
    print(f"The value '{repetitions}' does not exist in the tuple.")

# Input string
input_string = input("Enter a string: ")

# Initialize an empty dictionary to store character frequencies
char_frequency = {}

# Iterate through the string
for char in input_string:
    # Check if the character is already in the dictionary
    if char in char_frequency:
        # If it's in the dictionary, increment its count by 1
        char_frequency[char] += 1
    else:
        # If it's not in the dictionary, initialize its count to 1
        char_frequency[char] = 1

print("Character frequency in the string:")
for char, count in char_frequency.items():
    print(f"'{char}': {count}")

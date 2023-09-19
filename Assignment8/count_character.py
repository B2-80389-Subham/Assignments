def count_characters(s):
    s = s.lower()
    char_count = {}

    for char in s:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

    return char_count


input_string = input("Enter a string: ")
character_counts = count_characters(input_string)

print("Character counts:")
for char, count in character_counts.items():
    print(f"'{char}': {count}")

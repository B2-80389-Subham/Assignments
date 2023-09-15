def filter_long_words(input_list, filter_length):
    filtered_words = []

    for word in input_list:
        if len(word) > filter_length:
            filtered_words.append(word)

    return filtered_words


input_list = ["apple", "banana", "cherry", "date", "elderberry"]
filter_length = int(input("Enter the integer length: "))

result = filter_long_words(input_list, filter_length)
print(f"Words longer than {filter_length} characters: {result}")

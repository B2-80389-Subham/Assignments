def filter_long_words(word_list, length):
    filtered_words = []

    for word in word_list:
        if len(word) > length:
            filtered_words.append(word)

    return filtered_words


input_list = ["apple", "banana", "cherry", "date", "elderberry"]
filter_length = int(input("Enter the integer length: "))

result = filter_long_words(input_list, filter_length)
print(f"Words longer than {filter_length} characters: {result}")

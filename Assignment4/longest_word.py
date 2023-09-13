def longest_word(word_list):
    if len(word_list) == 0:
        return None

    longest_length = len(word_list[0])

    for word in word_list:
        if len(word) > longest_length:
            longest_length = len(word)

    return longest_length


word_list = ['kiti', 'citi', 'witty', 'deity', 'pretty']
longest_length = longest_word(word_list)

if longest_length is not None:
    print(f"The length of the longest word is: {longest_length}")
else:
    print("The list is empty.")

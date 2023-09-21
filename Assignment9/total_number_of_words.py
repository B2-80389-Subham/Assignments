def count_words_in_file(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
            words = text.split()
            word_count = len(words)
            return word_count
    except FileNotFoundError:
        print(f"File '{filename}' not found.")


filename = "your_text_file.txt"
total_words = count_words_in_file(filename)
print(f"Total number of words in '{filename}': {total_words}")

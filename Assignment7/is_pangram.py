def is_pangram(sentence):
    # Convert the sentence to lowercase to make it case-insensitive
    sentence = sentence.lower()

    # Initialize a set to store the unique letters in the sentence
    unique_letters = set()

    # Iterate through the characters in the sentence
    for char in sentence:
        # Check if the character is a lowercase letter
        if 'a' <= char <= 'z':
            # Add the lowercase letter to the set
            unique_letters.add(char)

    # Check if there are 26 unique lowercase letters (the entire alphabet)
    return len(unique_letters) == 26


# Test the function with a sentence
sentence = "The quick brown fox jumps over the lazy dog"
if is_pangram(sentence):
    print(f"'{sentence}' - is a pangram.")
else:
    print(f"'{sentence}' - is not a pangram.")

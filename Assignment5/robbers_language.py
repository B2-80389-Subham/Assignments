def is_consonant(char):
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    return char in consonants


def translate(text):
    translated_text = ''

    for char in text:
        if is_consonant(char):
            translated_text += char + 'o' + char
        else:
            translated_text += char

    return translated_text


original_text = "this is fun"
translated_text = translate(original_text)
print(translated_text)

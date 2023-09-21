text = "SHIFT"

for i in range(len(text)):
    rotated_text = text[i:] + text[:i]
    print(rotated_text)

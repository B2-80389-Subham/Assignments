def count_lines_not_starting_with_c(filename):
    count = 0
    try:
        with open(filename, 'r') as file:
            for line in file:
                cleaned_line = line.strip()
                if cleaned_line and not cleaned_line[0].lower() == 'c':
                    count += 1
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    return count


filename = "story.txt"
line_count = count_lines_not_starting_with_c(filename)
print(f"Number of lines not starting with 'C': {line_count}")

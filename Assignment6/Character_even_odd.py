def display_even_characters(input_string):
    even_characters = input_string[1::2]
    print("Characters from even positions:", even_characters)


def display_odd_characters(input_string):
    odd_characters = input_string[::2]
    print("Characters from odd positions:", odd_characters)


def display_string_length(input_string):
    length = len(input_string)
    print("Length of the string:", length)


def add_a_to_string(input_string):
    length = len(input_string)
    modified_string = input_string + 'a' * length
    print("Modified string:", modified_string)


while True:
    print("\nMenu:")
    print("A. Display characters from even position")
    print("B. Display characters from odd position")
    print("C. Display length of a string")
    print("D. Add 'a' at the end of string length times")
    print("E. Quit")

    choice = input("Enter your choice (A/B/C/D/E): ")

    if choice == 'A' or choice == 'a':
        input_string = input("Enter a string: ")
        display_even_characters(input_string)
    elif choice == 'B' or choice == 'b':
        input_string = input("Enter a string: ")
        display_odd_characters(input_string)
    elif choice == 'C' or choice == 'c':
        input_string = input("Enter a string: ")
        display_string_length(input_string)
    elif choice == 'D' or choice == 'd':
        input_string = input("Enter a string: ")
        add_a_to_string(input_string)
    elif choice == 'E' or choice == 'e':
        break
    else:
        print("Invalid choice. Please enter a valid option (A/B/C/D/E).")

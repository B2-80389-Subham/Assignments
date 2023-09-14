def count_frequency(numbers):
    frequency_dict = {}

    for number in numbers:
        if number in frequency_dict:
            frequency_dict[number] += 1
        else:
            frequency_dict[number] = 1

    return frequency_dict


numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 7, 6, 2, 4, 2, 5, 23, 6, 4]
frequency = count_frequency(numbers_list)

for number, count in frequency.items():
    print(f"{number}: {count} times")

even_numbers = []
odd_numbers = []

for i in range(6):
    num = int(input(f"Enter number {i + 1}: "))
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

result_dict = {'EVEN': even_numbers, 'ODD': odd_numbers}
print(result_dict)

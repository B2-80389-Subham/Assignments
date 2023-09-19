days_in_month = int(input("Enter the number of days in the month (between 28 and 31): "))
if 28 <= days_in_month <= 31:
    start_day = int(input("What day of the week month begins? \npress 0 : monday\npress 1 : tuesday"
                          "\npress 2 : wednesday\npress 3 : thursday\n"
                          "press 4 : friday\npress 5 : saturday\npress 6 : sunday\nyour input: "))
    days_of_week = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]
    for day in days_of_week:
        print(day, end=" ")
    print()
    current_day = 1
    for _ in range(start_day):
        print("  ", end=" ")
    for current_day in range(1, days_in_month + 1):
        print(str(current_day).rjust(2), end=" ")
        if (current_day + start_day) % 7 == 0:
            print()
    if (current_day + start_day) % 7 != 0:
        print()
else:
    print("Invalid input. The number of days in the month must be between 28 and 31.")

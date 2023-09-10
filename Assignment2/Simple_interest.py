def simple_interest_fun(principal, rate_of_interest, time):

    if principal < 0 or rate_of_interest < 0 or time < 0:
        return "Invalid input. All values should be non-negative."

    simple_interest = (principal * rate_of_interest * time) / 100
    return simple_interest


principal_amount = float(input("Enter the principal amount: "))
interest_rate = float(input("Enter the rate of interest (in percentage): "))
time_period = float(input("Enter the time period (in years): "))

result = simple_interest_fun(principal_amount, interest_rate, time_period)

if type(result) == str:
    print(result)
else:
    print(f"Simple Interest: {result:.2f}")

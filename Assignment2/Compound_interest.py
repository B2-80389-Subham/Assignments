def compound_interest_fun(principal, rate_of_interest, time):
    """
    This Function Calculates compound interest.
    Returns:
    float: The compound interest.
    """
    if principal < 0 or rate_of_interest < 0 or time < 0:
        return "Invalid input. All values should be non-negative."

    compound_interest = principal * ((1 + rate_of_interest / 100) ** time - 1)
    return compound_interest


principal_amount = float(input("Enter the principal amount: "))
interest_rate = float(input("Enter the rate of interest (in percentage): "))
time_period = float(input("Enter the time period (in years): "))

result = compound_interest_fun(principal_amount, interest_rate, time_period)

if type(result) == str:
    print(result)
else:
    print(f"Compound Interest: {result:.2f}")

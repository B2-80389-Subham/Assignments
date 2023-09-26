class Computation:
    def __init__(self):
        pass

    def sum_first_n_integers(self, n):
        if n < 1:
            return "N must be a positive integer"
        return sum(range(1, n + 1))


calculator = Computation()
n = int(input("Enter a number: "))
result = calculator.sum_first_n_integers(n)

print(f"The sum of the first {n} integers is: {result}")

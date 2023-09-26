class Computation:
    def __init__(self):
        pass

    def is_prime(self, num):
        if num <= 1:
            return False
        if num <= 3:
            return True

        if num % 2 == 0 or num % 3 == 0:
            return False

        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6

        return True

    def test_primes(self, num1, num2):
        if num1 >= num2:
            return "num1 must be less than num2"

        primes_between = []
        for num in range(num1 + 1, num2):
            if self.is_prime(num):
                primes_between.append(num)

        return primes_between


calculator = Computation()
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
prime_numbers_between = calculator.test_primes(num1, num2)

if prime_numbers_between:
    print(f"Prime numbers between {num1} and {num2}: {prime_numbers_between}")
else:
    print(f"No prime numbers found between {num1} and {num2}")

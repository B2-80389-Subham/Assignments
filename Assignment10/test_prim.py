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

    def testPrim(self, num):
        if num <= 0:
            return "Enter a positive integer"

        if self.is_prime(num):
            return f"{num} is a prime number"
        else:
            return f"{num} is not a prime number"


calculator = Computation()

# Test the testPrim method
num = int(input("Enter a number: "))
result = calculator.testPrim(num)

print(result)

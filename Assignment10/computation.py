class Computation:
    def __init__(self):
        pass

    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 == 0:
            return "Cannot divide by zero"
        return num1 / num2

    def power(self, base, exponent):
        return base ** exponent

    def modulus(self, num1, num2):
        if num2 == 0:
            return "Cannot calculate modulus with zero"
        return num1 % num2


calculator = Computation()

# Perform calculations
result1 = calculator.add(5, 3)
result2 = calculator.subtract(10, 4)
result3 = calculator.multiply(6, 7)
result4 = calculator.divide(20, 5)
result5 = calculator.power(2, 3)
result6 = calculator.modulus(15, 4)

# Print the results
print("Addition:", result1)
print("Subtraction:", result2)
print("Multiplication:", result3)
print("Division:", result4)
print("Exponentiation:", result5)
print("Modulus:", result6)

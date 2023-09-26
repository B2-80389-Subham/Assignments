class Computation:
    def __init__(self):
        pass

    def tableMult(self, num):
        if num <= 0 or num > 9:
            return "Enter a valid integer between 1 and 9"

        print(f"Multiplication Table for {num}:")
        for i in range(1, 11):
            result = num * i
            print(f"{num} x {i} = {result}")

    def allTablesMult(self):
        for i in range(1, 10):
            self.tableMult(i)
            print()


calculator = Computation()
num = int(input("Enter a number: "))
calculator.tableMult(num)
calculator.allTablesMult()

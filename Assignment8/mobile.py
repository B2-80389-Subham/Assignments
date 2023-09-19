class Mobile:
    def __init__(self):
        self.ModelName = ""
        self.Company = ""
        self.Price = 0.0

    def set_attributes(self, model_name, company, price):
        self.ModelName = model_name
        self.Company = company
        self.Price = price

    def print_details(self):
        print(f"Model Name: {self.ModelName}")
        print(f"Company: {self.Company}")
        print(f"Price: ${self.Price:.2f}")

    def can_afford(self, b):
        if self.Price <= b:
            return True
        else:
            return False


my_mobile = Mobile()
my_mobile.set_attributes("iPhone 15", "Apple", 999.99)
my_mobile.print_details()

budget = int(input("Enter the budget: "))
if my_mobile.can_afford(budget):
    print("You can afford this mobile.")
else:
    print("Sorry! insufficient budget.")

class BankAccount:
    def __init__(self, i=0.0):
        self.balance = i

    def deposit(self, a):
        if a > 0:
            self.balance += a
            print(f"Deposited ${a:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Invalid deposit amount. Please enter a positive amount.")

    def withdraw(self, a):
        if a > 0:
            if a <= self.balance:
                self.balance -= a
                print(f"Withdrew ${a:.2f}. New balance: ${self.balance:.2f}")
            else:
                print("Insufficient funds. Withdrawal canceled.")
        else:
            print("Invalid withdrawal amount. Please enter a positive amount.")


initial_balance = float(input("Enter initial balance: "))
my_account = BankAccount(initial_balance)

while True:
    print("Options:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Exit")
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        amount = float(input("Enter deposit amount: "))
        my_account.deposit(amount)
    elif choice == '2':
        amount = float(input("Enter withdrawal amount: "))
        my_account.withdraw(amount)
    elif choice == '3':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

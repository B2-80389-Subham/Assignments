class Account:
    def __init__(self, accHolderName, mobileNumber, accNumber, balance):
        self.accHolderName = accHolderName
        self.mobileNumber = mobileNumber
        self.accNumber = accNumber
        self.balance = balance


class Bank:
    def __init__(self, bankName, branchName, ifscCode):
        self.bankName = bankName
        self.branchName = branchName
        self.ifscCode = ifscCode
        self.accountList = []

    def print_bank_info(self):
        print("Bank Name:", self.bankName)
        print("Branch Name:", self.branchName)
        print("IFSC Code:", self.ifscCode)

    def add_account(self, account):
        if len(self.accountList) < 15:
            self.accountList.append(account)
            return True
        else:
            print("Cannot add more accounts. Limit reached.")
            return False

    def print_all_accounts(self):
        print("Accounts in the bank:")
        for account in self.accountList:
            print("Account Holder:", account.accHolderName)
            print("Account Number:", account.accNumber)
            print("Balance:", account.balance)
            print()

    def print_selected_account(self, accNumber):
        for account in self.accountList:
            if account.accNumber == accNumber:
                print("Account Holder:", account.accHolderName)
                print("Account Number:", account.accNumber)
                print("Balance:", account.balance)
                return
        print("Account not found.")

    def delete_account(self, accNumber):
        for account in self.accountList:
            if account.accNumber == accNumber:
                self.accountList.remove(account)
                print("Account deleted successfully.")
                return 1
        print("Account not found.")
        return 0

    def deposit_amount(self, accNumber, amount):
        for account in self.accountList:
            if account.accNumber == accNumber:
                account.balance += amount
                print("Amount deposited successfully.")
                return account.balance
        print("Account not found.")
        return None


my_bank = Bank("MyBank", "Main Branch", "IFSC12345")

account1 = Account("john", "1234567890", "1001", 5000)
account2 = Account("jane", "9876543210", "1002", 6000)
account3 = Account("randell", "5555555543", "1003", 7000)
account4 = Account("april", "9876584950", "1002", 4000)
account5 = Account("christin", "5598555567", "1003", 9000)

my_bank.add_account(account1)
my_bank.add_account(account2)
my_bank.add_account(account3)
my_bank.add_account(account4)
my_bank.add_account(account5)

while True:
    print("\nBanking Application Menu:")
    print("1. Print Bank Information")
    print("2. Add New Account")
    print("3. Print Information of All Accounts")
    print("4. Print Information of Selected Account")
    print("5. Delete Selected Account")
    print("6. Deposit Amount in Account")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        my_bank.print_bank_info()
    elif choice == "2":
        accHolderName = input("Enter Account Holder Name: ")
        mobileNumber = input("Enter Mobile Number: ")
        accNumber = input("Enter Account Number: ")
        balance = float(input("Enter Initial Balance: "))
        account = Account(accHolderName, mobileNumber, accNumber, balance)
        if my_bank.add_account(account):
            print("Account added successfully.")
    elif choice == "3":
        my_bank.print_all_accounts()
    elif choice == "4":
        accNumber = input("Enter Account Number: ")
        my_bank.print_selected_account(accNumber)
    elif choice == "5":
        accNumber = input("Enter Account Number to delete: ")
        deleted = my_bank.delete_account(accNumber)
        if deleted:
            print("Account deleted successfully.")
        else:
            print("Account not found.")
    elif choice == "6":
        accNumber = input("Enter Account Number to deposit into: ")
        amount = float(input("Enter Amount to Deposit: "))
        updated_balance = my_bank.deposit_amount(accNumber, amount)
        if updated_balance is not None:
            print("Updated Balance:", updated_balance)
    elif choice == "7":
        print("Exiting the application.")
        break
    else:
        print("Invalid choice. Please enter a valid option.")


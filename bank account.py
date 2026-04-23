class BankAccount:
    def __init__(self, name, account_no, balance):
        self.name = name
        self.account_no = account_no
        self.balance = balance

    # Display account details
    def display(self):
        print("\nAccount Holder:", self.name)
        print("Account Number:", self.account_no)
        print("Balance:", self.balance)

    # Deposit money
    def deposit(self, amount):
        self.balance += amount
        print("Amount deposited:", amount)
        print("New Balance:", self.balance)

    # Withdraw money
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn:", amount)
            print("Remaining Balance:", self.balance)
        else:
            print("Insufficient Balance")

    # Check balance
    def check_balance(self):
        print("Current Balance:", self.balance)


# Create account
name = input("Enter account holder name: ")
acc_no = input("Enter account number: ")
balance = float(input("Enter initial balance: "))

account = BankAccount(name, acc_no, balance)

while True:
    print("\n----- Bank Menu -----")
    print("1. Display Account Details")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        account.display()

    elif choice == 2:
        amt = float(input("Enter amount to deposit: "))
        account.deposit(amt)

    elif choice == 3:
        amt = float(input("Enter amount to withdraw: "))
        account.withdraw(amt)

    elif choice == 4:
        account.check_balance()

    elif choice == 5:
        print("Thank you for using the bank system.")
        break

    else:
        print("Invalid choice")
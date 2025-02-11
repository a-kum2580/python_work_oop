class BankAccount:
    def __init__(self, account_number, balance=0):
        self._account_number = account_number  # Encapsulation
        self._balance = balance  # Encapsulation

    def deposit(self, *args):
        # Simulate overloading by checking the number of arguments
        if len(args) == 1:
            amount = args[0]
            note = None
        elif len(args) == 2:
            amount, note = args
        else:
            print("Invalid number of arguments for deposit.")
            return

        if amount > 0:
            self._balance += amount
            print(f"Deposited UGX {amount} to account {self._account_number}. New balance: UGX {self._balance}")
            if note:
                print(f"Note: {note}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew UGX {amount} from account {self._account_number}. New balance: UGX {self._balance}")
        else:
            print("Invalid withdrawal amount or insufficient balance")

    def check_balance(self):
        print(f"Account {self._account_number} balance: UGX {self._balance}")
        return self._balance


class SavingsAccount(BankAccount):  # Inheritance
    def __init__(self, account_number, balance=0, interest_rate=0.05):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate  # Additional attribute for SavingsAccount

    def calculate_interest(self):
        interest = self._balance * self.interest_rate
        self.deposit(interest)
        print(f"Interest of UGX {interest} added. New balance: UGX {self._balance}")


class CheckingAccount(BankAccount):  # Inheritance
    def __init__(self, account_number, balance=0, overdraft_limit=50000):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit  # Additional attribute for CheckingAccount

    def withdraw(self, amount):  # Polymorphism
        if 0 < amount <= self._balance + self.overdraft_limit:
            self._balance -= amount
            print(f"Withdrew UGX {amount} from account {self._account_number}. New balance: UGX {self._balance}")
        else:
            print("Withdrawal amount exceeds overdraft limit")


# Dictionary to hold accounts
accounts = {}


def create_account():
    account_type = input("Enter account type (savings/checking): ").strip().lower()
    account_number = input("Enter account number: ").strip()
    if account_number in accounts:
        print("Account number already exists.")
        return
    if account_type == "savings":
        accounts[account_number] = SavingsAccount(account_number)
    elif account_type == "checking":
        accounts[account_number] = CheckingAccount(account_number)
    else:
        print("Invalid account type. Please choose 'savings' or 'checking'.")
        return
    print(f"{account_type.capitalize()} account {account_number} created.")


def deposit():
    account_number = input("Enter account number: ").strip()
    amount = float(input("Enter deposit amount: "))
    note = input("Enter a note for this transaction (optional): ").strip()

    if account_number in accounts:
        if note:
            accounts[account_number].deposit(amount, note)  # Call with two arguments
        else:
            accounts[account_number].deposit(amount)  # Call with one argument
    else:
        print("Account not found.")


def withdraw():
    account_number = input("Enter account number: ").strip()
    amount = float(input("Enter withdrawal amount: "))
    if account_number in accounts:
        accounts[account_number].withdraw(amount)
    else:
        print("Account not found.")


def check_balance():
    account_number = input("Enter account number: ").strip()
    if account_number in accounts:
        accounts[account_number].check_balance()
    else:
        print("Account not found.")


def user_interface():
    while True:
        print("\n--- Bank Account Manager ---")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")

        choice = input("Select an action (1-5): ").strip()

        if choice == '1':
            create_account()
        elif choice == '2':
            deposit()
        elif choice == '3':
            withdraw()
        elif choice == '4':
            check_balance()
        elif choice == '5':
            print("Exiting the Bank Account Manager.")
            break
        else:
            print("Invalid choice. Please select a valid option.")


# Run the user interface
user_interface()

class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited Rs.{amount}. New balance is Rs.{self.balance}.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdraw Rs.{amount}. New balance is Rs.{self.balance}.")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def check_balance(self):
        print(f"Current balance for account {self.account_number} is Rs.{self.balance}.")


# Use case
if __name__ == "__main__":
    # Creating a bank account
    account = BankAccount("1234567890", 1000)
    print("Account created with account number:", account.account_number)

    # Depositing money
    account.deposit(500)

    # Withdrawing money
    account.withdraw(200)

    # Checking balance
    account.check_balance()
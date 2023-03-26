from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
    
    @abstractmethod
    def deposit(self, amount):
        pass
    
    @abstractmethod
    def withdraw(self, amount):
        pass

class CheckingAccount(Account):
    def __init__(self, account_number, balance=0, overdraft_limit=1000):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if self.balance - amount >= -self.overdraft_limit:
            self.balance -= amount
        else:
            print("Withdrawal amount exceeds overdraft limit")

class SavingsAccount(Account):
    def __init__(self, account_number, balance=0, interest_rate=0.01):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
        else:
            print("Withdrawal amount exceeds account balance")

    def add_interest(self):
        self.balance += self.balance * self.interest_rate

class BusinessAccount(Account):
    def __init__(self, account_number, balance=0, transaction_limit=5000):
        super().__init__(account_number, balance)
        self.transaction_limit = transaction_limit
        self.transaction_count = 0
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if self.transaction_count >= self.transaction_limit:
            print("Transaction limit exceeded")
        elif self.balance - amount >= 0:
            self.balance -= amount
            self.transaction_count += 1
        else:
            print("Withdrawal amount exceeds account balance")

def atm():
    accounts = {}
    while True:
        print("\n==== ATM ====")
        print("1. Create account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check balance")
        print("5. Quit")
        choice = input("Enter choice (1-5): ")

        if choice == "1":
            print("\n==== CREATE ACCOUNT ====")
            account_type = input("Enter account type (checking, savings, business): ")
            account_number = input("Enter account number: ")
            if account_type == "checking":
                accounts[account_number] = CheckingAccount(account_number)
            elif account_type == "savings":
                accounts[account_number] = SavingsAccount(account_number)
            elif account_type == "business":
                accounts[account_number] = BusinessAccount(account_number)
            else:
                print("Invalid account type")
        
        elif choice == "2":
            print("\n==== DEPOSIT ====")
            account_number = input("Enter account number: ")
            if account_number in accounts:
                amount = float(input("Enter amount: "))
                accounts[account_number].deposit(amount)
            else:
                print("Account not found")

        elif choice == "3":
            print("\n==== WITHDRAW ====")
            account_number = input("Enter account number: ")
            if account_number in accounts:
                amount = float(input("Enter amount: "))
                accounts[account_number].withdraw(amount)
            else:
                print("Account not found")

        elif choice == "4":
            print("\n==== CHECK BALANCE ====")
            account_number = input("Enter account number: ")
            if account_number in accounts:
                print(f"Balance: ${accounts[account_number].balance:.2f}")
            else:
                print("Account not found")

        elif choice == "5":
            print("\nGoodbye!")
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    atm()
    
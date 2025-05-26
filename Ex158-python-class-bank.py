class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def __repr__(self):
        return "Test balance:%s" % (self.balance)

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}.")

class Bank:
    def __init__(self, accounts = {}):
        self.accounts = accounts

    def add_account(self, account_no, account: BankAccount):
        self.accounts[account_no] = account
        print(f"Account {account_no} added.")

    def remove_account(self, account_no):
        del self.accounts[account_no]
        print(f"Account {account_no} removed.")

    def get_accounts(self):
        print(f"{self.accounts}")


bank = Bank()
account_1 = BankAccount(100)
bank.add_account(1234, account_1)
account_2 = BankAccount(200)
bank.add_account(5678, account_2)
bank.get_accounts()
bank.remove_account(1234)
bank.get_accounts()

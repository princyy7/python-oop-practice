class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{self.owner}: Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdraw amount must be positive.")
        elif amount > self.balance:
            print(f"{self.owner}: Insufficient funds.")
        else:
            self.balance -= amount
            print(f"{self.owner}: Withdrew {amount}. New balance: {self.balance}")

    def transfer(self, other_account, amount):
        if amount <= 0:
            print("Transfer amount must be positive.")
        elif amount > self.balance:
            print(f"{self.owner}: Not enough balance to transfer.")
        else:
            self.balance -= amount
            other_account.balance += amount
            print(f"{self.owner} transferred {amount} to {other_account.owner}.")

    def show_balance(self):
        print(f"{self.owner}'s balance: {self.balance}")


# Create accounts
acc1 = BankAccount("Princy", 1000)
acc2 = BankAccount("Alex", 500)

# Before transfer
acc1.show_balance()
acc2.show_balance()

# Transfer money
acc1.transfer(acc2, 300)

# After transfer
acc1.show_balance()
acc2.show_balance()


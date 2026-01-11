class Account:
    def __init__(self, acc_no, name, balance=0):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposited {amount}")
        print(f"Deposit successful! New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdrew {amount}")
            print(f"Withdrawal successful! New balance: {self.balance}")

    def show_balance(self):
        print(f"Account {self.acc_no} | Balance: {self.balance}")

    def show_transactions(self):
        print("Transaction history:")
        for t in self.transactions:
            print("-", t)


# Example usage
acc1 = Account(1001, "Alice", 500)
acc1.deposit(200)
acc1.withdraw(100)
acc1.show_balance()
acc1.show_transactions()

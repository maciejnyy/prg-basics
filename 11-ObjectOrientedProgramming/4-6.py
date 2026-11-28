class BankAccount:
    def __init__(self, account_number):
        self.account_number = account_number
        self.balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds on the account")
        elif amount > 0:
            self.balance -= amount

    def display_info(self):
        formatted_balance = f"{self.balance:.2f}".replace(".", ",")
        print(f"Bank Account No: {self.account_number}")
        print(f"Balance: PLN {formatted_balance}")

def main():
    account = BankAccount("12 3456 5555 9090 1111 0000 7722")
    account.display_info()
    account.deposit(25.30)
    account.display_info()
    account.withdraw(31.70)
    account.display_info()
    account.withdraw(14)
    account.display_info()

if __name__ == "__main__":
    main()

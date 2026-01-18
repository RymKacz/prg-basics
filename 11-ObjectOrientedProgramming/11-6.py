class Bank_acc():
    def __init__(self,bank_acc_number):
        self.bank_acc_number = bank_acc_number
        self.current_balance = 0
    def deposit(self,amount):
        self.current_balance += amount
    def withdraw(self,amount):
        self.current_balance -= amount
    def display_info(self):
        print(f"Bank Account No: {self.bank_acc_number}")
        print(f"Balance: ${round(self.current_balance,2)}")
def main():
    my_account = Bank_acc("12 3456 5555 9090 1111 0000 7722")
    my_account.display_info()
    my_account.deposit(25.30)
    my_account.display_info()
    my_account.withdraw(31.70)
    my_account.display_info()
    my_account.withdraw(14)
    my_account.display_info()
if __name__ == "__main__":
    main()

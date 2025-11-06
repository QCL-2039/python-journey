class InSufficientBalance(Exception):
    pass

class Person:
    def __init__(self, name, no, balance):
        self.name = name 
        self.account_no = no
        self.balance = balance 

    def show_account_details(self):
        print(f"Account Holder: {self.name}, Account No: {self.account_no}, Balance: {self.balance}")

    def deposit(self, balance):
        self.balance += balance
        print(f"{balance} deposited. New balance: {self.balance}")

    def withdraw_balance(self, balance):
        try:
            if balance > self.balance or (self.balance - balance) <= 1000:
                raise InSufficientBalance(
                    "Withdrawal denied: amount exceeds balance or would reduce balance below 1000."
                )

            else:
                self.balance -= balance
                print(f"You have withdrawn {balance}. New balance: {self.balance}")
        except InSufficientBalance as obj:
            print(obj)


# Tester part
person = Person("Sohel Rana", "41220300573", 50000)
person.show_account_details()
person.withdraw_balance(49500)

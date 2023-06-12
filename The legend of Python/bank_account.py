class BankAccount:
    def __init__(self, first_name, last_name, account_id, account_tipe, pin, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.account_id = account_id
        self.account_tipe = account_tipe
        self.pin = pin
        self.balance = balance

    def deposit(self):
        money = int(input("How much would you like to deposit?: "))
        result = self.balance + money
        print(
            "Thank you! your deposit of: ",
            money,
            " was a succes!, your current balance is: ",
            result,
        )

    # return result

    def withdraw(self):
        ammount = int(input("How much you wanna retire?: "))
        result = self.balance - ammount
        print(
            "Thank you! your withdraw of: ",
            ammount,
            " was a succes!, your current balance is: ",
            result,
        )
        # return result

    def display_balance(self):
        print("your current balance is: ", self.balance)


Jonathan = BankAccount("Jonathan", "Medina", 5523654, "savings", 1234, 500)

Jonathan.deposit()
Jonathan.withdraw()
Jonathan.display_balance()

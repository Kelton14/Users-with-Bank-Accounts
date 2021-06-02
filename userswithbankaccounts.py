class BankAccount:
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if(self.balance <= amount):
            print("Insufficient funds: charging a $5 fee")
            self.balance -= 5
        else: 
            self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        if(self.balance > 0):
            x = self.balance * self.int_rate
            self.balance += x
        else: 
            self.balance = self.balance
        return self

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)

    def make_deposit(self, amount):
        self.account.deposit(amount)

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)

    def display_user_balance(self):
        print(f"{self.name}, Balance: ${self.account.balance}")

    def transfer_money(self, other_user, amount):
        self.account.balance += amount
        other_user.account.balance -= amount
        # return self
    
Tom = User("Tom" , "bigtom@gmail.com")
Sally = User("Sally", "supersally@outlook.com")
Bob = User("Bob", "bobbyboberson@aol.com")


Tom.make_deposit(600)
Tom.make_deposit(1500)
Tom.make_deposit(1)
Tom.make_withdrawal(34)
Tom.display_user_balance()

Sally.make_deposit(450)
Sally.make_deposit(975)
Sally.make_withdrawal(15)
Sally.make_withdrawal(245)
Sally.display_user_balance()

Bob.make_deposit(1500)
Bob.make_withdrawal(15)
Bob.make_withdrawal(15)
Bob.make_withdrawal(15)
Bob.display_user_balance()

Bob.transfer_money(Sally, 500)
Sally.display_user_balance()
Bob.display_user_balance()

import datetime

class BankAccount:
    def __init__(self):
        self.balance = 0
        self.transactions = []

    def deposit(self, amount):
        if amount<0:
            print("Negative Entry Not Allowed")
        else:
            self.balance += amount
            self.transactions.append((f"deposit :{amount} on {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"))
    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            self.transactions.append((f"withdraw {amount} on {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"))

    def show_balance(self):
        print(self.balance)

    def show_transaction_history(self):
       for i in self.transactions:
           print(i)

class SavingsAccount(BankAccount):
    def __init__(self,interest=5):
        super().__init__()
        self.interest_rate=interest


    def apply_interest(self):
        clac_interest=self.balance*self.interest_rate/100
        self.balance+=clac_interest
        self.transactions.append((f"apply {clac_interest} on {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"))


class CurrentAccount(BankAccount):
    def __init__(self,OverDraft=1000):
        super().__init__()
        self.OverDraft=OverDraft
    def withdraw(self,amount):
        if amount>self.OverDraft+self.balance:
            print("Insufficient funds")
        else:
          self.balance -= amount
          self.transactions.append((f"withdraw {amount} on {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"))



#b=BankAccount()
#c=SavingsAccount(5)
#c.deposit(1000)
#c.apply_interest()
#c.show_balance()
d=CurrentAccount()
d.deposit(2000)
d.withdraw(1000)
d.withdraw(2500)
d.show_balance()
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
    def __init__(self,intrest):
        super().__init__()
        self.intrest_rate=intrest


    def apply_intreset(self):
        clac_intrest=self.balance*self.intrest_rate/100
        self.balance+=clac_intrest




#b=BankAccount()
c=SavingsAccount(5)
c.deposit(1000)
c.apply_intreset()
c.show_balance()

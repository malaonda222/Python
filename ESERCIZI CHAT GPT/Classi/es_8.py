class BankAccount:
    def __init__(self, account_holder:str, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount:float):
        if amount > 0:
            self.balance += amount
            print(f"Deposito di {amount} effettuato.")
        else:
            print("Importo non valido.")
    
    def withdraw(self, amount:float):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount 
            print(f"La somma ritirata è {amount}.")
        else:
            print(f"Saldo insufficiente o importo non valido.")
           
    def get_balance(self):
        return self.balance 
    

account = BankAccount("Mario", 18000)
account.deposit(3000)
account.withdraw(8000)
print(f"Saldo attuale: {account.get_balance()}")
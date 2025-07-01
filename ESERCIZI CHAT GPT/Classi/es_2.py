class BankAccount:
    total_account = 0

    def __init__(self, balance:float):
        self.balance = balance
        BankAccount.total_account += 1

    @classmethod
    def get_total_account(cls):
        return cls.total_account
    
    @classmethod
    def interest_rate(cls):
        return cls.interest_rate
    
account1 = BankAccount(6000)
account2 = BankAccount(1300)

print(f"Il numero di account bancari è: {BankAccount.get_total_account()}")

print(f"Il tasso di interesse globale è: {BankAccount.interest_rate()}")
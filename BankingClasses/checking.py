from BankingClasses.banking import BankAccount

class CheckingAccount(BankAccount):
    def __init__(self, balance, overdraft_limit=100):
        super().__init__(balance)
        self.overdraft_limit: float = overdraft_limit
        
    def deposit(self, amount):
        self.balance += amount
        
    def withdraw(self, amount):
        if self.balance < amount + self.overdraft_limit:
            raise ValueError(f'You only have {self.balance:,.2f}!')
        else:
            self.balance -= amount
            
    def get_balance(self):
        return self.balance

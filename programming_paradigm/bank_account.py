class BankAccount:
    """A simple bank account class that handles deposits, withdrawals and balance display"""

    def __init__(self, initial_balance):
        """this initializes the bank account with an initial an optional balance. Default  balance is 0 if not specified  """
        self.account_balance = initial_balance

    def deposit(self,amount):
        """add money to the account balance


        
        """
        if amount > 0:
            self.account_balance += amount
        else:
            print("Deposit amount must be positive")
        
    def withdraw (self, amount):
        """
        remove money from account if sufficient funds are available
        """
        if amount <=0:
            print("withdrawal amount must be positive")
            return False
        if self.account_balance >=amount:
            self.account_balance -= amount
            return True
        return False
    
    def display_balance(self):
        """Displays the current balance in user friendly format"""

        print(f"current Balance : $({self.account_balance:.2f})")

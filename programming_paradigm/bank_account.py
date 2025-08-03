class BankAccount:
    """A simple bank account class that handles deposits, withdrawals, and balance display"""
    
    def __init__(self, initial_balance=0):
        """
        Initialize the bank account with an optional initial balance
        Default balance is 0 if not specified
        """
        self.account_balance = initial_balance
    
    def deposit(self, amount):
        """
        Add money to the account balance
        Args:
            amount (float): The amount to deposit (must be positive)
        """
        if amount > 0:
            self.account_balance += amount
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        """
        Remove money from the account if sufficient funds are available
        Args:
            amount (float): The amount to withdraw (must be positive)
        Returns:
            bool: True if withdrawal succeeded, False if insufficient funds
        """
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        if self.account_balance >= amount:
            self.account_balance -= amount
            return True
        return False
    
    def display_balance(self):
        """Display the current account balance in a user-friendly format"""
        print(f"Current Balance: ${self.account_balance:.2f}")
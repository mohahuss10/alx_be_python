#!/usr/bin/env python3
import sys
from bank_account import BankAccount

def main():
    # Initialize account with $100 starting balance
    account = BankAccount(100)
    
    # Check if command is provided
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)
    
    # Parse command and amount
    try:
        command, *params = sys.argv[1].split(':')
        amount = float(params[0]) if params else None
    except ValueError:
        print("Invalid amount format. Please use numbers.")
        sys.exit(1)
    
    # Execute commands
    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount:.2f}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount:.2f}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command. Use deposit, withdraw, or display.")

if __name__ == "__main__":
    main()
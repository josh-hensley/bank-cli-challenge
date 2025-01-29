"""This function handles the transfer process for the user."""
from BankingClasses.checking import CheckingAccount
from BankingClasses.savings import SavingsAccount
from BankingClasses.validation import Validation
from BankingFunctions.deposit import handle_deposit
from BankingFunctions.transfer import handle_transfer
from BankingFunctions.withdraw import handle_withdrawal

def main():
    """
    This function is the entry point of the banking system.
    It prompts the user to enter their email and password for authentication.
    If the email and password are valid, the default balances are shown.
    It then presents a menu of options to the user,
    allowing them to make deposits, withdrawals, or transfers between accounts.
    """
    email = input("Enter your email: ")
    print("Your password should be at least 8 characters long,\n", "contain at least one uppercase and lowercase letter,\n", "one number, and one of the following special characters:!@#$%^&*.")
    password = input("Enter your password: ")

    attempts = 1
    while attempts < 3:
        if Validation.validate_email(email) and Validation.validate_password(password):
            break
        else:
            print("Invalid email or password. Please try again.")
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            attempts += 1
    if attempts >= 3:
        print("Too many failed attempts...")

    # Set up accounts with default balances.
    checking_account = CheckingAccount(4321.00)
    savings_account = SavingsAccount(6543.21)

    # Print a message for the user inform them of their checking and savings balances
    print("Here are your account balances:")
    print(f'Checking: {checking_account.get_balance():,.2f}')
    print(f'Savings: {savings_account.get_balance():,.2f}')
    
    while True:
        try:
            print("What would you like to do?")
            print("1. Deposit\n2. Withdraw\n3. Transfer\n4. Quit")
            choice = input('Select a number.  ')
            if choice == 4:
                print('Have a nice day!')
                break
            elif choice == 1:
                handle_deposit(checking_account, savings_account)
            elif choice == 2:
                handle_withdrawal(checking_account, savings_account)
            elif choice == 3:
                handle_transfer(checking_account, savings_account)
            else:
                raise ValueError('Invalid choice!')
        except ValueError as e:
                print(e)
                continue

if __name__ == "__main__":
    main()

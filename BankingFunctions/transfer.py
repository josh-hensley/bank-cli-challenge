"""This function handles the transfer process for the user."""

def handle_transfer(checking, savings):
    """
    Handles the transfer of funds between checking and savings accounts.

    Parameters:
    - checking (Account): The checking account object.
    - savings (Account): The savings account object.

    The function prompts the user to select an account to make a transfer.
    It handles exceptions and prints error messages if the user enters invalid inputs.
    If the user enters 'q', the function returns and exits.
    If the user enters '1', the function asks for the withdrawal amount from the checking account.
    If the user enters '2', the function asks for the withdrawal amount from the savings account.
    After the transfer the function prints the updated balances of both accounts.
    If the user enters an invalid choice, the function displays an error message and prompts again.
    """
    print("Which account would you like to transfer from?")
    choice = input('1. Checking\n2. Savings\n3. Quit\n')
    if choice == 3:
        return

    try:
        if choice in [1,2]:
            try:
                amount = float(input("How much to transfer?  "))
            except ValueError as e:
                print('Error: ', e)
                handle_transfer(checking, savings)
                return
            if choice == 1:
                checking.withdraw(amount)
                savings.deposit(amount)
            else:
                savings.withdraw(amount)
                checking.deposit(amount)
            balances(checking, savings)
        else:
            raise ValueError('Invalid choice.')
    except ValueError as e:
        print(e)
        handle_transfer(checking, savings)

def balances(checking, savings):
    """This function prints the account balances for the user."""
    print("\nHere are your account balances:")
    print(f"Checking: ${checking.get_balance():,.2f}")
    print(f"Savings: ${savings.get_balance():,.2f}")

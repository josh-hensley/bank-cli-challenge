"""This function handles the withdrawal process for the user."""

def handle_withdrawal(checking, savings):
    """
    Handles the withdrawal of funds for checking and savings accounts.

    Parameters:
    - checking (CheckingAccount): The checking account object.
    - savings (SavingsAccount): The savings account object.

    The function prompts the user to select an account and make a withdrawal.
    It handles exceptions and prints error messages if the user enters invalid inputs.
    If the user enters 'q', the function returns and exits.
    If the user enters '1', the function asks for the withdrawal amount from the checking account.
    If the user enters '2', the function asks for the withdrawal amount from the savings account.
    After each withdrawal, the function prints the updated balance of the respective account.
    If the user enters an invalid choice, the function displays an error message and prompts again.
    """
    print("Which account would you like to make a withdrawal?")
    choice = input('1. Checking\n2. Savings\n3. Quit\n')
    if choice == 3:
        return

    try:
        if choice in [1,2]:
            try:
                amount = float(input('Withdraw what amount?  '))
                if choice == 1:
                    checking.withdraw(amount)
                elif choice == 2:
                    savings.withdraw(amount)
                else:
                    raise ValueError('Invalid Choice.')
            except ValueError as e:
                print('Error: ', e)
                handle_withdrawal(checking, savings)
                return
        else:
            raise ValueError('Invalid Choice.')
    except ValueError as e:
        print(e)
        handle_withdrawal(checking, savings)
        return

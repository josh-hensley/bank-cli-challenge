"""This function handles the deposit process for the user."""

# TODO: Build out the handle_deposit function
# TODO: Pass in the checking account and savings account objects.
def handle_deposit(checking, savings):
    """
    This function handles the deposit process for the user.

    Parameters:
    checking (Account): The checking account object.
    savings (Account): The savings account object.
    """
    print("Which account would you like to make a deposit?")
    choice = input('1. Checking\n2. Savings\n3. Quit\n')
    if choice == 3:
        return
    try:
        if choice in [1, 2]:
            amount = input("How much would you like to deposit?  ")
            try:
                if choice == 1:
                    checking.deposit(amount)
                    print(f'Current Balance now {checking.get_balance():,.2f}.')
                    return
                elif choice == 2:
                    print('Invalid amount.')
                    handle_deposit(checking, savings)
                    return
            # Use the ValueError as an exception.
            except ValueError:
                print('Invalid amount.')
                handle_deposit(checking, savings)
                return
        else:
            raise ValueError('Invalid Choice')
    # If the user enters an invalid choice,
    # Print the ValueError message and call the handle_deposit function recursively.
    except ValueError as e:
        print(e)
        handle_deposit(checking, savings)
        return

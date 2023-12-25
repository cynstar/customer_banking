"""Imports the SavingsAccount class and attributes from the Account.py file."""
# ADD YOUR CODE HERE
from Account import Account

class SavingsAccount(Account):
    def __init__(self, balance, interest, months):
        Account.__init__(self, balance, interest)

        self.months = months

# Define a function for the Savings Account
    def create_savings_account(balance, interest_rate, months):
        """Creates a savings account, calculates interest earned, and updates the account balance.

        Args:
            balance (float): The initial savings account balance.
            interest_rate (float): The APR interest rate for the savings account.
            months (int): The length of months to determine the amount of interest.

        Returns:
            float: The updated savings account balance after adding the interest earned.
            And returns the interest earned.
        """

        # Create an instance of the `Account` class and pass in the balance and interest parameters.
        #  Hint: You need to add the interest as a value, i.e, 0.
        # CE - I don't understand why I would use a numeric value to pass through rather than a variable? and I also don't understand why we pass anything to the Account file? It's not doing anything?
        # ADD YOUR CODE HERE
        savings_account = Account(balance, interest_rate)

    
        # Update the savings account balance by adding the interest earned
        # ADD YOUR CODE HERE
        # CE - I don't understand how I would get the interest earned from adding onto the balance?
        updated_balance = balance * (1 + interest_rate / 12) ** months

        
    # Calculate interest earned
        # ADD YOUR CODE HERE
        #CE - moved this below the updated balance, I needed the updated balance first in order to deduct from the original balance to get the earned interest...unless I misunderstand the intention.
        interest_earned = updated_balance - balance


        # Pass the updated_balance to the set balance method using the instance of the SavingsAccount class.
        # ADD YOUR CODE HERE
        savings_account.set_balance(updated_balance)


        # Pass the interest_earned to the set interest method using the instance of the SavingsAccount class.
        # ADD YOUR CODE HERE
        savings_account.set_interest(interest_earned)

        # Return the updated balance and interest earned.
        # return passed_balance, passed_earned
        return updated_balance, interest_earned
    
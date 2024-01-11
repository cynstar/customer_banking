# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from cd_account import CDAccount
from savings_account import SavingsAccount

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    savings_balance = float(input("Please enter your savings balance: "))
    #CE - converting user's percentage entry into a decimal
    savings_interest = float(input("Please enter the APR (%) for your savings account: "))
    # savings_interest = float(savings_interest) / 100
    savings_maturity = int((input("Please enter the number of months to calculate for your savings account: ")))

    # Call the create_savings_account function and pass the variables from the user.
    # create_savings_account(savings_balance, savings_interest, savings_maturity)
    updated_savings_balance, interest_earned = SavingsAccount.create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f'The interest earned in {savings_maturity} months is ${interest_earned:.2f} which generates a savings balance of ${updated_savings_balance:.2f}')

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    cd_balance = (float(input("Please enter your CD balance: ")))
    cd_interest = (float(input("Please enter the APR (%) for your CD account: "))) 
    cd_maturity = (int(input("Please enter the number of months to calculate for the CD: ")))
    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = CDAccount.create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
   
    print(f'The interest earned in {cd_maturity} months is ${interest_earned:.2f} which generates a CD balance of ${updated_cd_balance:.2f}')

if __name__ == "__main__":
    # Call the main function.
   main()

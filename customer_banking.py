# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from cd_account import create_cd_account
from savings_account import create_savings_account

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
    savings_interest = float(input("Please enter the APR (%) for your savings account: "))/100
    # savings_interest = float(savings_interest) / 100
    savings_maturity = int((input("Please enter the number of months to calculate for your savings account: ")))

    # Call the create_savings_account function and pass the variables from the user.
    # create_savings_account(savings_balance, savings_interest, savings_maturity)
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f'The interest earned in {savings_maturity} months is {interest_earned:.2f} for a total savings balance of {updated_savings_balance:.2f}')

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    cd_balance = (float(input("Please enter your CD balance: ")))
    cd_interest = (float(input("Please enter the APR (%) for your CD account: "))) / 100
    cd_maturity = (float(input("Please enter the number of months to calculate for the CD: ")))
    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f'The interest earned is {interest_earned} for a total CD amount of {updated_cd_balance} in {cd_maturity} months.')

if __name__ == "__main__":
    # Call the main function.
   main()

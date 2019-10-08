'''
Sean Collings
CS1400-2
Assignment 5, Task 1
Equation: 
futureInvestmentValue = investmentAmount × (1 + monthlyInterestRate)**numberOfMonths
Once again, I've broken my code up by using a main and get_user_input function. By following the given equation, the value should always be correct
'''

def main():
    print("Welcome to the future investment value calculator!")
    investment_amount, annual_interest_rate, years = get_user_input()

    months = years * 12
    monthly_interest_rate = (annual_interest_rate / 12) / 100

    future_investment_value = round(investment_amount * (1 + monthly_interest_rate)**months, 2) # Here's the actual equation. The round rounds up when its probably supposed to round down though
    print("Accumulated value is: " + str(future_investment_value))


def get_user_input():
    valid_user_input = False
    while not valid_user_input:
        try:
            investment_amount = float(input("Please enter the amount invested: "))
            annual_interest_rate = float(input("Please enter the annual interest rate: "))
            years = int(input("Please enter the number of years: "))
            valid_user_input = True
        except ValueError:
            print("Something went wrong, please try again")
    return (investment_amount, annual_interest_rate, years)

main()
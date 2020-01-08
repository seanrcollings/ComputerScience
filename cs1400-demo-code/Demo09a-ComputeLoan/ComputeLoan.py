'''
    This is Listing 2.8 in the book. The source code is also
    available online. Check Canvas for links to the book
    resources
'''

# Enter yearly interest rate
annualInterestRate = float(input(
    "Enter annual interest rate, e.g., 8.25: "))
monthlyInterestRate = annualInterestRate / 1200

# Enter number of years
numberOfYears = int(input(
    "Enter number of years as an integer, e.g., 5: "))

# Enter loan amount
loanAmount = float(input("Enter loan amount, e.g., 120000.95: "))

# Calculate payment
monthlyPayment = loanAmount * monthlyInterestRate / (1 - 1 / (1 + monthlyInterestRate) ** (numberOfYears * 12))
totalPayment = monthlyPayment * numberOfYears * 12

# Display results
print("The monthly payment is " +
      str(int(monthlyPayment * 100) / 100))
print("The total payment is " + str(int(totalPayment * 100) / 100))
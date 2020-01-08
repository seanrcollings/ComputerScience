'''
Sean Collings
CS1400-2
Assignment 6, Task 2

Requirment Specifications - Prompt the user to enter their name, number of 
hours worked in a week, hourly pay rate, fedral tax witholding rate, and state
tax witholding rate. Use these values to calculate their gross pay; fedral, state, 
and total deductions; and net pay. Display this content in a readable manner to the user

Sytem Analysis:
    grossPay = hours * pay
    deductions equations = grossPay * deduction 
    netPay = Gross pay - totalDeduction

System design:
    - Take in input for their name, number of hours worked in a week, 
    hourly pay rate, fedral tax witholding rate, and state tax witholding 
    rate.
    - Calculate gross pay
    - Calculate fedra, state, and total deductions
    - Subtract total deductions from gross pay
    - Output that to the user

Tests:
Test 1
    Input: hours = 40, pay = 12.75, federal = 0.11, state = .07
    output: net_pay = 418.20 (if this value is correct, all the others should be too)
    Passed
Test 2
    Input: hours = 25, pay = 20, federal = .13, state = .05
    Output: net_pay = 410
'''

def main():
    print("Please enter the employee's information: ")
    name, hours, pay, federal_withholdings, state_withholdings = get_user_input()

    gross_pay = hours * pay

    federal_deduction = gross_pay * federal_withholdings
    federal_percent = "(%s)" %(format(federal_withholdings, "0.1%"))

    state_deduction  = gross_pay * state_withholdings
    state_percent = "(%s)" % (format(state_withholdings, "0.1%"))

    total_deduction = federal_deduction + state_deduction
    net_pay = gross_pay - total_deduction

    message = format(name.upper() + " INFORMATION", "^80s")
    message += "\n\n"
    message += format("Pay", "^65s")
    message += "\n"
    message += format_line("Hours Worked", hours, False)
    message += format_line("Pay Rate", pay)
    message += format_line("Gross Pay", gross_pay)
    message += "\n"
    message += format("Deduction", "^65s")
    message += "\n"
    message += format_line("Federal Withholding " + federal_percent, federal_deduction)
    message += format_line("State Withholding " + state_percent, state_deduction)
    message += format_line("Total Deduction", total_deduction)
    message += "\n"
    message += format_line("Net Pay", net_pay)

    print(message)
            

def get_user_input():
    valid_user_input = False
    while not valid_user_input:
        try:
            name = input("Enter employee's name: ")
            hours = int(input("Enter the hours worked in a week: "))
            pay = float(input("Enter the hourly pay: "))
            federal_withholdings = float(input("Enter federal tax withholding rate (ex. 0.12): "))
            state_withholdings = float(input("Enter state tax withholding rate (ex. 0.06): "))
            valid_user_input = True 
        except ValueError:
            print("Something went wrong, please try again")
    return (name, hours, pay, federal_withholdings, state_withholdings)


def format_line(name, value, is_money=True): # since most of the lines get formatted the same, I wrote a little function to handle that
    if is_money: # quick fix for hours worked so it doesn't display the $
        name = format(name + ": $", '>40s') 
    else:
        name = format(name + ":  ", '>40s')
    value = format(value, '>15.2f')
    return name + value + "\n"

main()
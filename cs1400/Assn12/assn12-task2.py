from account import Account

def main():
    account = Account(10, 12.32, 4.2)

    while True:
        print('_______________________')
        print('ACCOUNTING INFORMATION')
        print('_______________________')
        print("(1): Display ID")
        print("(2): Display Balance")
        print("(3): Display Annual Interest Rate")
        print("(4): Display Monthly Interest Rate")
        print("(5): Display Monthly Interest")
        print("(6): Withdraw Money")
        print("(7): Deposit Money")
        print("(8): Exit ")
        print('_______________________')

        menu = eval(input("Enter a selection: "))
        print("#######################")
        if menu == 1: 
            print("ID: {}".format(account.getId()))
        elif menu == 2:
            print("BALANCE: {}$".format(account.getBalance()))
        elif menu == 3:
            print("ANNUAL INTEREST RATE: {0:.2f}%"
                .format(account.getAnnualInterestRate() * 100))
        elif menu == 4:
            print("MONTHLY INTEREST RATE: {0:.2f}%"
                .format(account.getMonthlyInterestRate() * 100))
        elif menu == 5:
            print("MONTHLY INTEREST: {0:.2f}$"
                .format(account.getMonthlyInterest()))
        elif menu == 6:
            print("How much do you want to withdraw?")
            print("You're current balance is: {}".format(account.getBalance()))
            withdraw = float(input(">>> "))
            account.withdraw(withdraw)
            print("You're current balance is: {}".format(account.getBalance()))
        elif menu == 7:
            print("How much do you want to deposit?")
            print("You're current balance is: {}".format(account.getBalance()))
            deposit = float(input(">>> "))
            account.deposit(deposit)
            print("You're current balance is: {}".format(account.getBalance()))
        elif menu == 8:
            print("Goodbye!")
            exit()
        else:
            print("You did not enter expected input, please try again")
        
main()
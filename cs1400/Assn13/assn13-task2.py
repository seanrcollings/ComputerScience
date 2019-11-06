from password import Password

def main():
    done = False
    password = Password()
    print("Welcome to the password setter!")
    while not done:
        newPassword = input("Please enter a password: ")

        if password.setPassword(newPassword.strip('\n')):
            print("No problems with the password!")
            print("Password has been set ")
        else:
            print("Your password could not be set for the following reasons")
            print(password.getErrorMessage())

        cont = input("Do you want to make a new password (y/n) : ")
        if cont in ('n', 'no'):
            print("Goodbye!")
            done = True
        else:
            password.setErrorMessage([])

main()
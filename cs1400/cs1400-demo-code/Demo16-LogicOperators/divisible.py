import sys

input = input("Enter an integer: ")

if(not input.isdigit()):
    print("Invalid input")
    sys.exit(1)

input = eval(input)

if(input % 2 == 0):
    print(input, "is divisible by 2")

if(input % 2 == 0 and input % 5 == 0):
    print(input, "is divisible by 2 and 5")

if(input % 2 == 0 or input % 5 == 0):
    print(input, "is divisible by 2 or 5")

if(input % 2 == 0 or input % 5 == 0) and not (input % 2 == 0 and input % 5 == 0):
    print(input, "is divisible by 2 or 5 but not both")
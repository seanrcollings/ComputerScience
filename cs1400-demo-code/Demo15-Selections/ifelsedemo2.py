import random

num1 = random.randint(0, 99)
num2 = random.randint(0, 99)

userAnswer = input("What is " + str(num1) + " + " + str(num2) + "? ")

if userAnswer.isdigit():
    userAnswer = eval(userAnswer)
    actualAnswer = num1 + num2

    if userAnswer == actualAnswer:
        message = "correct!"
    else:
        message = "incorrect."

    print("Your answer is", message)
else:
    print("Your input is not valid")
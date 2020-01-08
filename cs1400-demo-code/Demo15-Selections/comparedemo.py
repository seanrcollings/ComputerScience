import random

num1 = random.randint(0, 99)
num2 = random.randint(0, 99)

userAnswer = eval(input("What is " + str(num1) + " + " + str(num2) + "? "))
actualAnswer = num1 + num2

isCorrect = userAnswer == actualAnswer

print("Your answer is", isCorrect)
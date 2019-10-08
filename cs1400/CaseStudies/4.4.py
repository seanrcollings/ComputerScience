from random import randint

num1 = randint(1, 99)
num2 = randint(1, 99)
num_sum = num1 + num2

user_input = int(input("What is the sum of %s and %s? " %(num1, num2)))

if user_input == num_sum:
    print("You are correct!")
else:
    print("You are incorrect :(")

print("The number is " + str(num_sum))
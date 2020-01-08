import random

number = random.randint(0, 100)

print("Guess a number between 0 and 100")

guess = -1  # this will make sure loop is always false, but lets us initialize

while guess != number:
    guess = int(input("What is your guess? "))

    if guess == number:
        print("You're right!")
    elif guess < number:
        print("You're too low")
    else:
        print("You're too high")
'''
Sean Collings
CS1400-2
Assignment 7, Task 1

Requirements Specificiation - Write a program that plays the popular scissor-rock-paper game. (A scissor can cut a paper, a rock can knock
a scissor, and a paper can wrap a rock.) The program randomly generates a number 0 , 1 , or 2 representing scissor, rock, 
and paper. The program prompts the user to enter a number 0 , 1 , or 2 and displays a message indicating whether the user 
or the computer wins, loses, or draws. Here are sample runs:

System Analysis - use randint function to generate the random number; use a dictionary to make the conditional checks shorter and easier

System design 
    1: Generate a random number from 0 - 2
    2: Prompt user for their input (0, 1, 2)
    3: Check to see who wone
    4: Display those results to the user

Testing:
    Test 1:
        Input - 0
        passed
    Test 2:
        input - 1
        passed
    Test 3:
        input - 2
        passed

'''
from random import randint

def main():
    print("Welcome to this sweet rock, paper, scissors game")
    game_dict = {
        0: {"name": "rock", "beats": 2}, 
        1: {"name": "paper", "beats": 0},
        2: {"name": "scissors", "beats": 1}
    }

    player_choice = get_user_input() # users choice
    computer_choice = randint(0, 2) # computers choice

    # checks for win state
    if game_dict[player_choice]['beats'] == computer_choice:
        result = "You won!"
    elif game_dict[computer_choice]['beats'] == player_choice:
        result = "You Lose :("
    else:
        result = "Tie"

    print("The Computer is %s. You are %s. %s" %(game_dict[computer_choice]['name'], game_dict[player_choice]['name'], result))


def get_user_input():
    valid_user_input = False
    while not valid_user_input:
        try:
            player_choice = int(input("Please enter rock (0), paper (1), or scissors (2): "))
            if player_choice in (0, 1, 2):
               valid_user_input = True
            else:
                print("The number you entered is not 0, 1, or 2")
        except ValueError:
            print("What you entered was not a number, please try again")
    return player_choice

main()
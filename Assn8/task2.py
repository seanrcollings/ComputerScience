'''
Sean Collings
CS1400-2
Assignment 8, Task 2

1 - Requirment Specifcations
	prompt the user if they want to change their choice
	Run through 100,000 games with those options; aggregating the results
	Calculate the percent they got the car, and percent they got the goat
	Output that to the user

2 - System analysis
	Loopy boys

3 - System Design
	1 - Prompt the use if they would like to change their choice 
	2 - Run a for loop 100,000 times simlulating the game with those choices 
	3 - On each loop randomly select which door has the car  and the goats 
	4 - if the user wants to switch, switch them
	5 - aggregate the wins and losses

5 - Testing
	Output: Should lean in the direction of 2:1
	passed: 
	Wins: 66761 / 100,000
	Losses: 33239 / 100,000

This program asks the user if they want to switch their choice. If they do, it chooses one to open then picks the other 
door that wasn't opened. It returns True or false based on if the pick was the car, these results then get aggregated into
wins and losses
'''
import random

def sim_game_show(switch: bool) -> bool: # I just learned about type hints, and wanted to try them out
	doors = ['goat', 'goat', 'car'] # The order is always static, if it's shuffled it throws off the results (not sure why though)
	chosen_door = random.randint(1, 3)
	# I used list comprehensions to reduce the number of lines the program had
	revealed_door = [num for num in range(1, 4) if num not in (chosen_door, doors.index('car'))][0] 

	if switch:
		chosen_door = [num for num in range(1, 4) if num not in (chosen_door, revealed_door)][0]
	return chosen_door == doors.index('car')


def main():
	print("Here's a cool game with goats")
	while True:
		user_input = input("Do you want to switch each round? (y/n) : ")
		switch = True if user_input == 'y' or user_input == 'yes' else False
		wins = 0
		losses = 0

		for i in range(0, 100000):
			if sim_game_show(switch):
				wins += 1
			else:
				losses += 1

		print("Wins: "   + format(wins / 100000, '0.3%'))
		print("Losses: " + format(losses / 100000, '0.3%'))

		play_again = input("Play again (y/n)? ")
		if play_again == 'n' or play_again == 'no':
			break
main()
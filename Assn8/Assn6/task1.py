'''
Sean Collings
CS1400-2
Assignment 6, Task 1

1. Requirments specification - This program takes the number of sides and
the length of those sides of the regular polygon they want to calculate the
area of. Then it calculates the area using the formula below

2. System Analysis
area = (numberOfSides * sideLength**2) / (4 * tan(pi / numberOfSides)) 

3. System design
 1. Prompt the user for number of sides and side lengths of the regular poloygon from the user
 2. Convert user input into floats
 3. plug those values into the equation for area
 4. print the result to the user

5. Testing
    Test 1
        Input: Sides = 5, Side length = 5.5
        Output: 52.04444
        Failed: Since the tan function returns a complex, I had to change to just getting the real part
    Test 2 
        Input: Sides = 8, Side length = 6.5
        Output: 204.00105
        Passed
'''
import math
from cmath import tan

def main():
    print("Ready to calculate the area of a regular polygon?")

    sides, side_length = get_user_input()
    area = (sides * math.pow(side_length, 2)) / (4 * tan(math.pi / sides).real)
    print("The area of the regular polygon is: " + str(round(area, 5)))

def get_user_input():
    valid_user_input = False
    while not valid_user_input:
        try:
            sides = float(input('Please enter the number of sides: '))
            side_length = float(input('Please enter the side length: '))
            valid_user_input = True
        except ValueError:
            print("Something went wrong, please try again")
    return (sides, side_length)

main()
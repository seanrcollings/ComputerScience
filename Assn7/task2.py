'''
Sean Collings
CS1400-2
Assignment 7, Task 1

Requirements Specification - Write a program that prompts the user to enter the center coordinates 
and radii of two circles  and determines whether the second circle is inside the first or overlaps with the first 

System Analysis - circle2 is inside circle1 if the distance between the two centers <= | r1 - r2| 
and circle2 overlaps circle1 if the distance between the two centers <= r1 + r2 
Calculate distance using: Square root of: (x2 - x1) ** 2 + (y2 - y1) ** 2

System Design - Prompt the user for the two circle centers and their radii
check to see if they overlap or if one is inside of the other
Display that result to the user.

Testing - 
    Test 1:
        Circle 1: (5, 2), 10
        Circle 2: (5, 3), 4
        Expected Output: Circle 2 is inside of circle 1
    Test 2:
        Circle 1: (10, 4), 5
        Circle 2: (10, 7), 6
        Expected output: The circle overlap
'''
from math import sqrt
import turtle # for visual representation

tr = turtle.Turtle()

def main():
    circle1_rad, circle1_x, circle1_y, circle2_rad, circle2_x, circle2_y = get_user_input() # users choice
    distance = calc_distance(circle1_x, circle1_y, circle2_x, circle2_y)
    
    # I added a visual representation fo the circle to check the logic, but left it in because it made sense
    tr.speed(0)
    draw(lambda: tr.circle(circle1_rad), (circle1_x, circle1_y - circle1_rad), 'red')
    draw(lambda: tr.circle(circle2_rad), (circle2_x, circle2_y - circle2_rad), 'blue')

    print("Check graphics output for visual representation :) (Cirlce 1 = red, Circle 2 = blue)")
    if distance <= abs(circle2_rad - circle1_rad):
        print("The second circle is inside of the first circle")
    elif distance <= circle1_rad + circle2_rad:
        print("The second circle is overlapping the first circle")
    else:
        print("The circle are not overlapping at all")

    turtle.mainloop()

def calc_distance(x1, y1, x2, y2): 
    # while not striclyt necessary, I find it nice to break out things like this into their own functions when possible
    distance = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance

def move_pen(x=0, y=0): # moves the pen without drawing lines between points
    tr.penup()
    tr.goto(x, y)
    tr.pendown()

def draw(action, location, color):
    move_pen(location[0], location[1]) # location[0] = x, location[1] = y
    tr.color(color)
    tr.begin_fill()
    action() # turtle function to actually draw something like circle
    tr.end_fill()

def get_user_input():
    valid_user_input = False
    while not valid_user_input:
        try:
            circle1_data = input("Please enter the radius and x, y coordinates for the first circle (eg: 1, 2, 3): ").split(',')
            circle1_rad = float(circle1_data[0])
            circle1_x = float(circle1_data[1]) 
            circle1_y = float(circle1_data[2])

            circle2_data = input("Please enter the radius and x, y coordinates for the second circle (eg: 1, 2, 3): ").split(',')
            circle2_rad = float(circle2_data[0])
            circle2_x = float(circle2_data[1]) 
            circle2_y = float(circle2_data[2])
            valid_user_input = True
        except ValueError:
            print("Something went wrong, please try again, please try again")
    return (circle1_rad, circle1_x, circle1_y, circle2_rad, circle2_x, circle2_y)

main()
'''
Sean Collings
CS1400-2
Assignment 5, Task 2
For this assignment, I've reused a few functions from the previous turtle assignment (move_pen, and draw)
I also once again have a get_user_input function that will prevent the program from crashing if the user enters non-valid data (not necessary, just for fun)
main just calls get_user_input, then draws the target based on those values
'''
import turtle

tr = turtle.Turtle()
tr.speed(0)


def main():
    print("Want to make a target? Boy do I got the program for you!")

    x, y, radius = get_user_input()
    current_radius = radius * 4 # radius of the current circle being drawn, starts with the largest circle and works inward

    draw(lambda: tr.circle(current_radius), (x, y - current_radius), "black")
    current_radius -= radius
    draw(lambda: tr.circle(current_radius), (x, y - current_radius), "blue")
    current_radius -= radius
    draw(lambda: tr.circle(current_radius), (x, y - current_radius), "red")
    current_radius -= radius
    draw(lambda: tr.circle(current_radius), (x, y - current_radius), "yellow")

    turtle.mainloop()


def get_user_input():
    valid_user_input = False
    while not valid_user_input:
        try:
            location = input("Please enter the location of the center of the bulls eye (x, y): ").split(",")
            # converts to a float, strips the parens if the user adds those, but they don't have to
            x = float(location[0].lstrip("(")) 
            y = float(location[1].rstrip(")"))
            diamater = float(input("Please enter the diamter of the center circle: "))
            valid_user_input = True
        except ValueError:
            print("Something went wrong, please try again")
    return (x, y, diamater / 2)

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

main()
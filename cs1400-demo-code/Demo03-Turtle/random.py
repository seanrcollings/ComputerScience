"""
This is simple demo of the turtle module. Note that in demo code I will not comment very much normally. This is so
you can learn by reading the code, not just by reading what the code should be doing. You should comment more than
what you see in the demos.
"""

# turtle is a library module that we want to use, so first we need to import it
import turtle

# Create a turtle. We'll call it 'tr'. You can name it something else
tr = turtle.Turtle()

# The first step is to show the turtle
tr.showturtle()

# Move the turtle forward 100 places
tr.forward(100)

# Turn to the right 90 degrees
tr.right(90)

# Move forward 50 places
tr.forward(50)

# Change the color
tr.color("red")

# Draw a circle
tr.circle(200)

# Move the turtle
tr.goto(-100, 100)

# Turn drawing off
tr.penup()

# Move in a circle
tr.circle(200)

# In PyCharm the program will end automatically, so we can add this to prevent that from happening
turtle.done();
''' Sean Collings 
CS1400-2
Assignment 4 Task 1
For my snowman, I decided to write a few functions to make the going a bit easier on me.
While its probably not the most effecient way for this to be done, the functions did 
When calling the draw function, I use Python's anonymous function lambda for the func arguement, 
which allows me to essentially pass a callback function into the draw function with arguments already in them '''

import turtle 
tr = turtle.Turtle()
turtle.bgcolor("black")
tr.speed(0) # the default speed is pretty slow, enabling this helped

def move_pen(x=0, y=0): # moves the pen without drawing lines between points
    tr.penup()
    tr.goto(x, y)
    tr.pendown()

def draw(action, location, color):
    move_pen(location[0], location[1])
    tr.color(color)
    tr.begin_fill()
    action()
    tr.end_fill()

def draw_rectangle(length, height, heading=0): # draws a rectangle, starting from top left and working it's way around clockwise
    tr.setheading(heading) # set the direction of the pen, by default is 0 and will draw a normal rectangle
    tr.forward(length)
    tr.right(90)
    tr.forward(height)
    tr.right(90)
    tr.forward(length)
    tr.right(90)
    tr.forward(height)

draw(lambda: tr.dot(300), (0, 500), "white") # draw head
draw(lambda: tr.dot(600), (0, 100), "white") # draw center body
draw(lambda: tr.dot(750), (0, -450), "white") # draw bottom body

draw(lambda: draw_rectangle(150, 200), (-80, 800), "#3D2817") # draws part 1 of the hat
draw(lambda: draw_rectangle(250, 80), (-130, 670), "#3D2817") # draws part 2 of the hat

draw(lambda: tr.dot(50), (-100, 500), "black") # draw right eye
draw(lambda: tr.dot(50), (100, 500), "black") # draw right eye
draw(lambda: draw_rectangle(200, 2, 5), (-100, 450), "black") # draw mouth, he's not the happiest snowman :/

draw(lambda: tr.dot(40), (0, 200), "black") # draw first button
draw(lambda: tr.dot(40), (0, 100), "black") # draw second button
draw(lambda: tr.dot(40), (0, 0), "black") # draw third button

draw(lambda: draw_rectangle(300, 10, 10), (-600, 100), "#3D2817") # draw right arm 
draw(lambda: tr.dot(75), (-600, 100), "#3D2817") # draw left hand
# draw left hand's fingers
draw(lambda: draw_rectangle(50, 10, -30), (-670, 150), "#3D2817")
draw(lambda: draw_rectangle(50, 10, 0), (-670, 110), "#3D2817")
draw(lambda: draw_rectangle(50, 10, 30), (-670, 80), "#3D2817")

draw(lambda: draw_rectangle(300, 10, 15), (300, 100), "#3D2817") # draw left arm
draw(lambda: tr.dot(75), (600, 170), "#3D2817") # draw left hand
# draw left hand's fingers
draw(lambda: draw_rectangle(50, 10, 30), (600, 200), "#3D2817")
draw(lambda: draw_rectangle(50, 10, 0), (630, 160), "#3D2817")
draw(lambda: draw_rectangle(50, 10, -30), (600, 150), "#3D2817")

turtle.mainloop()
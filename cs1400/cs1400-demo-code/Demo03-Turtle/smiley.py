"""
I didn't put comments in here so you can read/modify the code to figure out
what everything means
"""

import turtle

# setup turtle
tr = turtle.Turtle()
tr.showturtle()

# move to start location
tr.penup()
tr.goto(-200, -100)

# draw head
tr.pendown()
tr.begin_fill()
tr.fillcolor("yellow")
tr.circle(100)
tr.end_fill()

# move to eye location
tr.penup()
tr.goto(-240, 0)

# draw eye
tr.pendown()
tr.begin_fill()
tr.fillcolor("black")
tr.circle(20)
tr.end_fill()

# move to other eye location
tr.penup()
tr.goto(-160, 0)

# draw other eye
tr.pendown()
tr.begin_fill()
tr.circle(20)
tr.end_fill()

# move to mouth
tr.penup()
tr.goto(-260, -40)

# draw mouth
tr.setheading(315)
tr.pendown()
tr.width(10)
tr.circle(90, 90)

# hide the turtle
tr.hideturtle()

# cleanup (optional in Phanon, required in PyCharm)
turtle.done()
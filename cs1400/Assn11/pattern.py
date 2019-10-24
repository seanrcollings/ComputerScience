import turtle
from random import randint

tr = turtle.Turtle()

def setup():
    tr.speed(0)
    turtle.screensize(1000, 800)

def reset():
    tr.reset()
    setup()

def done():
    turtle.done()

def drawRectanglePattern(centerX, centerY, offset, width, height, count, rotation):
    currentRotation = 0     
    for i in range(count):
        tr.setheading(currentRotation)
        tr.penup()
        tr.goto(centerX, centerY)
        tr.forward(offset)
        tr.pendown()
        drawRectangle(width, height, rotation)
        currentRotation += 360 / count

def drawRectangle(width, height, rotation):
    tr.color(setRandomColor())
    tr.left(rotation) # sets to relevant rotation angle
    tr.forward(width)
    tr.left(90)
    tr.forward(height)
    tr.left(90)
    tr.forward(width)
    tr.left(90)
    tr.forward(height)

def drawCirclePattern(centerX, centerY, offset, radius, count):
    currentRotation = 0     
    for i in range(count):
        tr.setheading(currentRotation)
        tr.penup()
        tr.goto(centerX, centerY)
        tr.forward(offset)
        tr.right(90)
        tr.pendown()
        drawCircle(radius) 
        currentRotation += 360 / count

def drawCircle(radius):
    tr.color(setRandomColor())
    tr.circle(radius)

def drawSuperPattern(num = 1):
    # turtle.tracer(False) # Turns off the animation, so it doesn't take so long if you draw a lot of random shapes
    funcs = (drawRectanglePattern, drawCirclePattern) 
    for i in range(num):
        func = funcs[randint(0, 1)]
        if func == drawCirclePattern:
            drawCirclePattern(randint(-500, 500),
                randint(-300, 300),
                randint(-200, 200),
                randint(2, 100),
                randint(2, 200))
        if func == drawRectanglePattern:
            drawRectanglePattern(randint(-500, 500),
                randint(-300, 300),
                randint(-200, 200),
                randint(10, 200),
                randint(10, 200),
                randint(2, 200),
                randint(-360, 360))

def setRandomColor():
    color = "#%06x" % randint(0, 0xFFFFFF) # generates a hex code for a color randomly
    return color
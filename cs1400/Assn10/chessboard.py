import turtle

tr = turtle.Turtle()
tr.speed(0)

def drawChessboard(startX, startY, width=250, height=250):
    startX, startY = eval(startX), eval(startY)
    movePen(startX, startY)
    rectWidth, rectHeight = width // 8, height // 8
    drawRectangle(rectWidth * 8 , rectHeight * 8 ) # draws outline

    drawAllRectangles(startX, startY, rectWidth, rectHeight)
    turtle.done()

def drawAllRectangles(startX, startY, rectWidth, rectHeight):
    movePen(startX, startY)
    currentX, currentY = startX, startY
    for i in range(8):
        if i % 2 == 0: # checks for even rows, which have a white starting square
            currentX += rectWidth

        movePen(currentX, currentY)

        for i in range(4):
            tr.color("black")
            tr.begin_fill()
            drawRectangle(rectWidth, rectHeight)
            tr.end_fill()

            currentX += rectWidth * 2
            movePen(currentX, currentY)

        currentX = startX
        currentY += rectHeight

def drawRectangle(width, height):
    tr.setheading(0) # set the direction of the pen, by default is 0 and will draw a normal rectangle
    tr.forward(width)
    tr.left(90)
    tr.forward(height)
    tr.left(90)
    tr.forward(width)
    tr.left(90)
    tr.forward(height)

def movePen(x=0, y=0): # moves the pen without drawing lines between points
    tr.penup()
    tr.goto(x, y)
    tr.pendown()
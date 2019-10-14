import turtle

tr = turtle.Turtle()
turtle.bgcolor("grey")
tr.speed(0)

def drawChessboard(startX, startY, width=250, height=250):
    move_pen(startX, startY)
    draw_rectangle(width, height)

    drawAllRectangles(startX, startY, width // 8, height // 8)
    turtle.done()

def drawAllRectangles(startX, startY, rectWidth, rectHeight):
    currentX, currentY = startX, startY
    for i in range(8):
        move_pen(currentX, currentY)

        color = "black" if i % 2 ==  0 else "white"
        for i in range(8):
            tr.color(color)
            tr.begin_fill()
            draw_rectangle(rectWidth, rectHeight)
            tr.end_fill()

            color = "white" if color == "black" else "black"
            currentX += rectWidth
            move_pen(currentX, currentY)

        currentX = startX
        currentY += rectHeight

def move_pen(x=0, y=0): # moves the pen without drawing lines between points
    tr.penup()
    tr.goto(x, y)
    tr.pendown()

def draw_rectangle(length, height, heading=0): # draws a rectangle, starting from top left and working it's way around clockwise
    tr.setheading(heading) # set the direction of the pen, by default is 0 and will draw a normal rectangle
    tr.forward(length)
    tr.left(90)
    tr.forward(height)
    tr.left(90)
    tr.forward(length)
    tr.left(90)
    tr.forward(height)

drawChessboard(-200, 200)

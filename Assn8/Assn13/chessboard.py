import turtle

class Chessboard:
    def __init__(self, tr, startX, startY, width=250, height=250):
        self.__tr = tr
        self.__tr.speed(0)

        self.__startX = startX
        self.__startY = startY
        self.__width = width
        self.__height = height
        self.__rectWidth = width // 8
        self.__rectHeight = height // 8

    def draw(self):
        self.__movePen(self.__startX, self.__startY)
        self.__drawRectangle(self.__width, self.__height) # draws outline
        self.__drawAllRectangles()

    def __drawAllRectangles(self):
        self.__movePen(self.__startX, self.__startY)
        currentX, currentY = self.__startX, self.__startY
        for i in range(8):
            if i % 2 == 0: # checks for even rows, which have a white starting square
                currentX += self.__rectWidth

            self.__movePen(currentX, currentY)

            for i in range(4):
                self.__tr.color("black")
                self.__tr.begin_fill()
                self.__drawRectangle(self.__rectWidth, self.__rectHeight)
                self.__tr.end_fill()

                currentX += self.__rectWidth * 2
                self.__movePen(currentX, currentY)

            currentX = self.__startX
            currentY += self.__rectHeight

    def __drawRectangle(self, width, height):
        self.__tr.setheading(0) # set the direction of the pen, by default is 0 and will draw a normal rectangle
        self.__tr.forward(width)
        self.__tr.left(90)
        self.__tr.forward(height)
        self.__tr.left(90)
        self.__tr.forward(width)
        self.__tr.left(90)
        self.__tr.forward(height)

    def __movePen(self, x=0, y=0): # moves the pen without drawing lines between points
        self.__tr.penup()
        self.__tr.goto(x, y)
        self.__tr.pendown()
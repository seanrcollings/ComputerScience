'''Contains the rectangle class'''
class Rectangle:
    '''Rectangle class, able to draw itself when drawn a turtle object'''
    def __init__(self, x, y, height, width, color):
        self.__x = x
        self.__y = y
        self.__height = height
        self.__width = width
        self.__color = color

    def __str__(self):
        return "Rectangle: x: {} | y: {} | height: {} | width: {} | color: {} | ".format(
            self.__x, self.__y, self.__height, self.__width, self.__color)

    def draw(self, tr):
        tr.penup()
        tr.goto(self.__x, self.__y)
        tr.pendown()
        tr.color(self.__color)
        tr.begin_fill()
        tr.forward(self.__width)
        tr.left(90)
        tr.forward(self.__height)
        tr.left(90)
        tr.forward(self.__width)
        tr.left(90)
        tr.forward(self.__height)
        tr.end_fill()
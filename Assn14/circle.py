
class Circle:
    def __init__(self, x, y, radius, color):
        self.__x = x
        self.__y = y
        self.__radius = radius
        self.__color = color

    def __str__(self):
        return "Circle: x: {} | y: {} | radius: {} | color: {} | ".format(
            self.__x, self.__y, self.__radius, self.__color)

    def draw(self, tr):
        tr.penup()
        tr.goto(self.__x, self.__y - self.__radius)
        tr.pendown()
        tr.color(self.__color)
        tr.begin_fill()
        tr.circle(self.__radius)
        tr.end_fill()

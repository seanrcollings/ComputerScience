from math import pi 

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def getRadius(self):
        return self.radius

    def getArea(self):
        return pi * self.radius ** 2

    def getPerimeter(self):
        return 2 * pi * self.radius
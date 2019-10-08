import math


class Circle:
    def __init__(self, radius):
        self.radius = radius # This is an instance variable
        otherRadius = radius # This is a local variable

    def getPerimeterInstanceVariable(self):
        # Instance variables are in scope throughout the class
        return 2 * math.pi * self.radius

    def getPerimeterLocalVariable(self):
        # Local variables are only in scope in the function
        # So this wouldn't work
        return 2 * math.pi * otherRadius



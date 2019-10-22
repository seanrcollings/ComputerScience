class Circle:
    def __init__(self, radius):
        self.radius = radius

    def getRadius(self):
        return self.radius

circle = Circle(100)
circle.getRadius() # return 100
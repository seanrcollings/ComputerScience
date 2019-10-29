from math import pi 

class Circle:
    def __init__(self, radius):
        self.__radius = radius

    def getRadius(self):
        return self.__radius

    def getArea(self):
        return pi * self.radius ** 2

    def getPerimeter(self):
        return 2 * pi * self.radius

class Employee:
    def __init__(self, name, sal):
        self.__name=name  # private attribute 
        self.__salary=sal # private attribute

e1 = Employee("Sean", 1000)
print(e1.__salary) # will return an attribue error
print(e1._Employee__salary) # Can still access the private varible as such object._class__variable


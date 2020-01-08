import math


def main():
    # This is an actual Circle object
    circle_1 = Circle(5)

    print("The area is", circle_1.get_area())
    print("The perimeter is", circle_1.get_perimeter())
    # The data and functions are tied together (encapsulated)


class Circle():
    def __init__(self, radius):
        self.__radius = radius

    def get_area(self):
        return math.pi * self.__radius ** 2

    def get_perimeter(self):
        return math.pi * 2 * self.__radius


main()
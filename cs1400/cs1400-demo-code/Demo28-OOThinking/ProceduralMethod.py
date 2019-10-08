import math


def main():
    circle_1 = 5 # This is just data that represents a radius

    print("The area is", calc_area(circle_1))
    print("The perimeter is", calc_perimeter(circle_1))
    # The data and functions are separate

def calc_area(radius):
    return math.pi * radius ** 2


def calc_perimeter(radius):
    return math.pi * 2 * radius


main()
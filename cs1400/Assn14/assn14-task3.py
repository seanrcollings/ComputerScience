from turtle import Turtle
from circle import Circle
from rectangle import Rectangle


def main():
    shapes = []
    tr = Turtle()
    tr.speed(0)

    done = False
    while not done:
        print("1) Enter Circle")
        print("2) Enter Rectangle")
        print("3) Remove Shape")
        print("4) Draw Shapes")
        print("5) Exit")

        menu = input("Enter a selection: ")

        if menu == '1':
            position = input("Please enter positon (x, y): ")
            x, y = [int(num) for num in position.split(',')]
            radius = int(input("Please enter a radius (5): "))
            color = input("Please enter a color (red, yellow, blue, and green only): ")

            shapes.append(Circle(x, y, radius, color))
            print("Circle added!")

        elif menu == '2':
            position = input("Please enter positon (x, y): ")
            x, y = [int(num) for num in position.split(',')]
            dimensions = input("Please enter dimensions (width, height) ")
            width, height = [int(num) for num in dimensions.split(',')]
            color = input("Please enter a color (red, yellow, blue, and green only): ")

            shapes.append(Rectangle(x, y, width, height, color))
            print("Circle Added")

        elif menu == '3':
            tr.clear()

        elif menu == '4':
            for shape in shapes:
                shape.draw(tr)

        elif menu == '5':
            print("Goodbye")
            done = True

        else:
            print("Input not recognized")

main()
from circle import Circle

def main():
    cir1 = Circle()
    cir2 = Circle(5)

    print("Circle 1", cir1.getPerimeter())
    print("Circle 2", cir2.getPerimeter())

    cir1.setRadius(20)
    print("Circle 1", cir1.getPerimeter())


main()
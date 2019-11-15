from cuboid import Cuboid


def main():
    dimensions = input("Please enter cube1's dimensions (ex: length, width, height): ")
    length, width, height = [float(dimension) for dimension in dimensions.split(',')]
    cube1 = Cuboid(length, width, height)

    dimensions = input("Please enter cube2's dimensions (ex: length, width, height): ")
    length, width, height = [float(dimension) for dimension in dimensions.split(',')]

    cube2 = Cuboid(length, width, height)

    print("Cube 1: " + str(cube1))
    print("Cube 2: " + str(cube2))
    print("Cube 1 + Cube 2: " + str(cube1 + cube2))
    print("Cube 1 - Cube 2: " + str(cube1 - cube2))
    print("Cube 1 == Cube 2: " + str(cube1 == cube2))
    print("Cube 1 > Cube 2: " + str(cube1 > cube2))
    print("Cube 1 < Cube 2: " + str(cube1 < cube2))

main()
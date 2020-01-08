class Cuboid:
    def __init__(self, length, width, height):
        self.__length = length
        self.__width = width
        self.__height = height

    def __str__(self):
        return "Length: {} | Width: {} | Height: {} | Surface Area: {} | Volume: {}".format(
            self.__length, self.__width, self.__height, len(self), self.getVolume())

    def __len__(self):
        return int(2 * self.__length * self.__width + 2 * self.__length * \
            self.__height + 2 * self.__height* self.__width)

    def __add__(self, other):
        volume = self.getVolume() + other.getVolume()
        cubedRoot = volume ** (1 / 3)
        return Cuboid(cubedRoot, cubedRoot, cubedRoot)

    def __sub__(self, other):
        volume = self.getVolume() - other.getVolume()
        cubedRoot = volume ** (1 / 3)
        return Cuboid(cubedRoot, cubedRoot, cubedRoot)

    def __eq__(self, other):
        return self.getVolume() == other.getVolume()

    def __gt__(self, other):
        return self.getVolume() > other.getVolume()

    def __lt__(self, other):
        return self.getVolume() < other.getVolume()

    def getVolume(self):
        return self.__length * self.__width * self.__height

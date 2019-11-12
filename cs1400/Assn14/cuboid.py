class Cuboid:
    def __init__(self, length, width, height):
        self.__length = length
        self.__width = width 
        self.__height = height

    def __str__(self):
        return "Length: {} | Width: {} | Height: {} | Surface Area: {} | Volume: {}".format(
            self.__length, self.__width, self.__height, len(self), self.getVolume())
         

    def __len__(self):
        return 2 * self.__length * self.__width + 2 * self.__length * self.__height + 2 * self.__height* self.__width

    def __add__(self, other):
        # volume = self.getVolume() + other.getVolume()
        # cubedRoot = volume ** (1. / 3)
        # return Cuboid(cubedRoot, cubedRoot, cubedRoot) 
        length = self.__length + other.getLength()
        width = self.__width + other.getWidth()
        height = self.__height + other.getHeight()
        return Cuboid(length, width, height)

    def __sub__(self, other):
        length = self.__length - other.getLength()
        width = self.__width - other.getWidth()
        height = self.__height - other.getHeight()
        if length <= 0 or width <= 0 or height <= 0:
            return "Cannot create a cuboid with negative or zero dimensions"
        else:
            return Cuboid(length, width, height)

    def __eq__(self, other):
        if self.__length == other.getLength and self.__height == other.getHeight and self.__width == other.getWidth:
            return True
        else:
            return False
    
    def __gt__(self, other):
        volume = self.getVolume()
        otherVolume = other.getVolume()
        if volume > otherVolume:
            return True
        else:
            return False

    def __lt__(self, other):
        volume = self.getVolume()
        otherVolume = other.getVolume()
        if volume < otherVolume:
            return True
        else:
            return False


    def getLength(self):
        return self.__length

    def getWidth(self):
        return self.__width

    def getHeight(self):
        return self.__height

    def getVolume(self):
        return self.__length * self.__width * self.__height
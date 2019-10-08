def main():
    cir1 = Circle(50)
    print("Public Radius: ", cir1.pub_radius)

    print("Private Radius: ", cir1.__priv_radius)
    # The private radius can't be accessed outside the class

    print("Private Radius: ", cir1.get_priv_radius())
    # This works because I used a public method to get it

    print("Private Method: ", cir1.__priv_method())
    # Private methods can't be accessed outside the class


class Circle():
    def __init__(self, radius):
        self.__priv_radius = radius
        self.pub_radius = radius

    def get_priv_radius(self):
        # I can call a private method inside the class
        self.__priv_method()

        # Private radius can be accessed inside the class
        return self.__priv_radius

    def __priv_method(self):
        print("This is a private method")


main()

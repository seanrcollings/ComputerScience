# Define operators with dunders
# Look at all the possibilities listed in Chapter 8
class Widget:
    def __init__(self, value):
        self.__value = value

    def get_value(self):
        return self.__value

    def __add__(self, other):
        return self.__value + other.get_value()

    def __str__(self):
        return "I'm a widget with value " + str(self.__value)

    def __len__(self):
        return self.__value * 6


def main():
    widget_1 = Widget(10)
    widget_2 = Widget(25)

    print(widget_1 + widget_2)
    print(widget_1)
    print(widget_2.__str__())
    print(len(widget_1))
    print(widget_2.__len__())


main()
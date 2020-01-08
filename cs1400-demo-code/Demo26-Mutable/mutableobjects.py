class Widget:
    def __init__(self, width=10, height=10, depth=10):
        self.width = width
        self.height = height
        self.depth = depth

    def getVolume(self):
        return self.width * self.height * self.depth


def main():
    # Widgets are mutable objects
    widget1 = Widget()
    widget2 = Widget(50, 20, 5)

    print("Widget 1:", widget1.getVolume())
    useWidget(widget1)
    print("Widget 1:", widget1.getVolume())

    print("Widget 2:", widget2.getVolume())
    useWidget(widget2)
    print("Widget 2:", widget2.getVolume())


def useWidget(widget):
    widget.width = widget.width * 0.8
    widget.height = widget.height * 0.6
    widget.depth = widget.depth * 0.5


main()
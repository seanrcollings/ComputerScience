from gronkyutil import paw, coin

class Card:
    def __init__(self, _id):
        self.__id = _id
        self.__value = self.setValue()
        self.__paw = paw[self.__id // 40]
        self.__coin = coin[0 if self.__id % 2 == 0 else 1]


    def __str__(self):
        return "{} | {} | {}".format(
            format(str(self.__value), ">3s"),
            format(self.__paw, "^8s"),
            self.__coin)

    def __eq__(self, other):
        return self.__id == other.getID()

    def __gt__(self, other):
        return self.__id > other.getID()

    def __lt__(self, other):
        return self.__id < other.getID()

    def getID(self):
        return self.__id

    def getPaw(self):
        return self.__paw

    def getValue(self):
        return self.__value

    def getCoin(self):
        return self.__coin

    def setValue(self):
        value = self.__id
        while value >= 40:
            value -= 40
        if value % 2 == 0:
            return int((value + 2) / 2)
        else:
            return int((value + 1) / 2)

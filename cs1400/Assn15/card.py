from gronkyutil import paw, coin, maxCardValue
from math import ceil

bordersList = [0, 20, 40, 60, 80, 100, 120]

class Card:
    def __init__(self, _id):
        self.__id = _id
        self.__paw = paw[self.__id // 40]
        self.__coin = self.setCoin()
        self.__value = self.setValue()



    def __str__(self):
        return "{} | {} | {}".format(
            format(str(self.__value), ">3s"),
            format(self.__paw, "^8s"),
            self.__coin)

    def getID(self):
        return self.__id

    def getPaw(self):
        return self.__paw

    def getValue(self):
        return self.__value

    def setCoin(self):
       pass

    def setValue(self):
        for index in range(len(bordersList) - 1):
            if bordersList[index] <= self.__id < bordersList[index + 1]:
                return self.__id - (bordersList[index] - 1)



print("ID   VAL     PAW      COIN")
for i in range(0, 120):
    print(format(str(i), "<3s"), str(Card(i)))
    # Card(i)
print("ID   VAL     PAW      COIN")
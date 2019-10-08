class Card:
    __SUITS = ["Spades", "Clubs", "Hearts", "Diamonds"]
    __RANKS = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen",
                    "King"]

    def __init__(self, value):
        self.__value = value

    def getRank(self):
        return Card.__SUITS[self.__value % 13]

    def getSuit(self):
        return Card.__RANKS[self.__value // 13]

    def getCardValue(self):
        return self.__value % 13 + 1

    def getDeckValue(self):
        return self.__value

    # Dunder to return a string representation to print() and format()
    def __str__(self):
        return self.getRank() + " of " + self.getSuit()

    # Dunder to return a string representation to other usages
    def __repr__(self):
        return self.__str__()


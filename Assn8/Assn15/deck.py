from random import shuffle
from card import Card

class Deck:
    def __init__(self):
    	self.__cards = [Card(i) for i in range(0, 120)]

    def shuffle(self):
    	shuffle(self.__cards)
    	print("Cards have been shuffled")

    def draw(self):
    	return self.__cards.pop(0)

    def returnCards(self, *cards):
        for card in cards:
            self.__cards.append(card)
        print("All cards added")




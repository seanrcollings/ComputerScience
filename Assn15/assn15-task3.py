from deck import Deck
from card import Card
from gronkyutil import paw, coin, convertCardToValue

def main():
    deck = Deck()
    deck.shuffle()
    hand = [deck.draw() for i in range(30)]

    done = False
    while not done:
        print("1) Sort by value")
        print("2) Sort by ID")
        print("3) Find Card")
        print("4) New hand")
        print("5) Quit")
        menu = input(">>> ")

        if menu == '1':
            insertionSort(hand)
            displaHand(hand)

        elif menu == '2':
            bubbleSort(hand)
            displaHand(hand)

        elif menu == '3':
            cardValue = int(input("Value: "))

            print("Paw: ")
            print("1) Rock")
            print("2) Paper")
            print("3) Scissors")
            cardPaw = paw[int(input(">>> ")) - 1]

            print("Coin Face")
            print("1) Heads")
            print("2) Tails")
            cardCoin = coin[int(input(">>> ")) - 1]

            bubbleSort(hand)
            searchCard = Card(convertCardToValue(cardValue, cardPaw, cardCoin) )
            print("\nThat card is in the deck\n") if binarySearch(hand, searchCard) else print("\nThat card is not in the deck\n")


        elif menu == '4':
            print("New hand")
            deck.returnCards(*hand)
            deck.shuffle()
            hand = [deck.draw() for i in range(30)]

        elif menu == '5':
            print("Goodbye!")
            done = True

        else:
            print("Input not recognized")

def displaHand(inputList):
    print("VAL     PAW      COIN")
    for card in inputList:
        print(card)
    print("VAL     PAW      COIN")


def insertionSort(inputList):
    for i in range(1, len(inputList)):
        currElement = inputList[i]
        j = i - 1
        while j >= 0 and inputList[j].getValue() > currElement.getValue():
            inputList[j + 1] = inputList[j]
            j -= 1

        inputList[j + 1] = currElement


def bubbleSort(inputList):
    didSwap = True
    while didSwap:
        didSwap = False
        for num in range(len(inputList) - 1):
            if inputList[num] > inputList[num + 1]:
                inputList[num], inputList[num + 1] = inputList[num + 1], inputList[num]
                didSwap = True


def binarySearch(inputList, key):
    bottom = 0
    top = len(inputList) - 1

    while top >= bottom:
        mid = (bottom + top) // 2
        if inputList[mid] == key:
            return True
        elif inputList[mid] > key:
            top = mid - 1
        elif inputList[mid] < key:
            bottom = mid + 1

    return False

main()
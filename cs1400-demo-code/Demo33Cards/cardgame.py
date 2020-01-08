from DemoCode.Demo33Cards.deck import Deck


def main():
    deck = Deck()

    dealerHand = []
    playerHand = []

    for i in range(2):
        playerHand.append(deck.draw())
        dealerHand.append(deck.draw())

    print(playerHand)
    print(dealerHand)


main()
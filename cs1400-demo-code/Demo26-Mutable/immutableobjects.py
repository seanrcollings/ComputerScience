def main():
    # Numbers are immutable objects
    life1 = 100
    life2 = 500

    print("Life 1:,", life1)
    useLife(life1)
    print("Life 1:,", life1)

    print("Life 2:", life2)
    useLife(life2)
    print("Life 2:", life2)


def useLife(life):
    life = life * 0.8

main()
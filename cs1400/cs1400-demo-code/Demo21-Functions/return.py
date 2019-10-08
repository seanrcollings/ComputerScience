def withReturn():
    print("I will return a value")
    return 10


def noReturn():
    print("I do not return anything")


def main():
    print(withReturn())
    print(noReturn())


main()

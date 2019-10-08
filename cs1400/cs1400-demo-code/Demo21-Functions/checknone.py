import random


def favNum():
    num = random.randint(0, 5)
    if num != 2:
        return num
    else:
        return

def main():
    res = favNum()
    if res == None:
        print("You don't have a favorite number")
    else:
        print("Your favorite number is", res)


main()

import sys

birthYear = input("What year were you born? ")

if not birthYear.isdigit():
    print("That is not a valid year")
    sys.exit()

zodiac = int(birthYear) % 12

print("Year of the ", end="")

if zodiac == 0:
    print("Monkey")
elif zodiac == 1:
    print("Rooster")
elif zodiac == 2:
    print("Dog")
elif zodiac == 3:
    print("Pig")
elif zodiac == 4:
    print("Rat")
elif zodiac == 5:
    print("Ox")
elif zodiac == 6:
    print("Tiger")
elif zodiac == 7:
    print("Rabbit")
elif zodiac == 8:
    print("Dragon")
elif zodiac == 9:
    print("Snake")
elif zodiac == 10:
    print("Horse")
elif zodiac == 11:
    print("Sheep")

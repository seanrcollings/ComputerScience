'''
    This is the same as the positionandkeyword.py program except food now has a default argument
'''

def info(name, age, food="Spaghetti"):
    print(name + " is " + str(age) + " years old and likes to eat " + food.lower())


def main():
    info("George", 20, "Pizza")
    info(food="SOUP", age=12, name="Liz")
    info("Walter", food="Eggs", age=50)
    info("Jane", 23)


main()
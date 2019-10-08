import random

def main():
    list_1 = [[],[]]
    print("A list of two empty lists")
    print(list_1, end="\n")

    # Create an empty list then create 10 empty lists inside it
    list_2 = []

    for i in range(10):
        list_2.append([])
    print("A list appended with 10 empty lists")
    print(list_2)

    for i in range(len(list_2)):
        for j in range(10):
            list_2[i].append(random.randint(0, 9))
    print("A list of lists filled with random numbers")
    print(list_2)


main()
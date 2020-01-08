import random


def main():
    list_1 = []
    for i in range(5):
        list_1.append([])
        for j in range(10):
            list_1[i].append(random.randint(0, 10))

    #Access by index
    print("Access by Index")
    for i in range(len(list_1)):
        for j in range(len(list_1[i])):
            print(list_1[i][j], end=" ")
        print()

    #Access by element
    print("\nAccess by Element")
    for row in list_1:
        for num in row:
            print(num, end=" ")
        print()

main()
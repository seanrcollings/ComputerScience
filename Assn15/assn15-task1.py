def main():
    baseList = list(range(1, 101))

    list1 = [i for i in baseList if i % 2 == 0]
    print(list1)

    list2 = [i for i in baseList if i % 3 == 0 and i < 50]
    print(list2)

    list3 = [i * 10 for i in baseList if i % 5 == 0 and i > 50]
    print(list3)

main()
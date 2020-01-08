def main():
    lst = [134, 701, 233, 736, 275, 430, 977, 800, 233, 565, 947, 395, 379, 944, 765, 710, 361, 116, 194, 428, 973, 512, 649, 541, 116, 173, 863, 654, 502, 620, 545, 160, 340, 349, 533, 442, 141, 949, 57, 705, 236, 337, 922, 336, 119, 892, 311, 743, 331, 674, 221, 733, 59, 398, 390, 532, 659, 108, 228, 876, 102, 235, 148, 55, 667, 750, 515, 595, 610, 313, 705, 35, 474, 819, 549, 737, 61, 518, 939, 257, 622, 828, 721, 496, 82, 780, 554, 76, 240, 847, 675, 444, 557, 886, 812, 55, 91, 674, 130, 742]

    selectionSort(lst)
    for num in lst:
        print(num)


def selectionSort(inputList):
    for i in range(len(inputList) - 1):
        currMinIndex = i

        for j in range(i + 1, len(inputList)):
            if inputList[currMinIndex] > inputList[j]:
                currMinIndex = j

        if currMinIndex != i:
            inputList[i], inputList[currMinIndex] = inputList[currMinIndex], inputList[i]


main()
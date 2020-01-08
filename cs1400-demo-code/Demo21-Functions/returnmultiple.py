def threeSort(first, second, third):
    small = first
    mid = second
    big = third

    if small > mid:
        small, mid = mid, small

    if mid > big:
        mid, big = big, mid

    if small > mid:
        small, mid = mid, small

    return small, mid, big


def main():
    num1, num2, num3 = eval(input("Enter three numbers separated by a comma: "))
    num1, num2, num3 = threeSort(num1, num2, num3)

    print("In order: ", num1, num2, num3)


main()
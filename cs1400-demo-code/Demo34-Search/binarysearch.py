def main():
    list_1 = [1, 4, 6, 8, 29, 30, 43, 76, 85]
    key = 43
    result = binary_search(list_1, key)
    if result == -1:
        print("Did not find", key)
    else:
        print("Found,", key, "at position", result)


def binary_search(input_list, key):
    print(input_list)
    low = 0
    high = len(input_list) - 1
    while high >= low:
        print(low, high)
        mid = (high + low) // 2
        if key == input_list[mid]:
            return mid
        elif key < input_list[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return -1


main()
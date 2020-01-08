def main():
    list_1 = [4, 6, 1, 43, 1, 76, 85, 30, 8, 29]
    key = 85
    result = linear_search(list_1, key)
    if result == -1:
        print("Did not find", key)
    else:
        print("Found,", key, "at position", result)


def linear_search(input_list, key):
    for i in range(len(input_list)):
        if key == input_list[i]:
            return i
    return -1


main()
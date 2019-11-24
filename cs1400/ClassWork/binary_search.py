import random 

def binarySearchRecur(input_list, key):
    mid = (len(input_list) - 1) // 2

    if mid < 0:
        return False

    elif input_list[mid] == key:
        return True
    elif input_list[mid] > key:
        return binarySearchRecur(input_list[:mid], key)
    elif input_list[mid] < key:
        return binarySearchRecur(input_list[mid + 1:], key)


def binarySearchIter(inputList, key):
    bottom = 0
    top = len(inputList) - 1

    while top >= bottom:
        mid = (bottom + top) // 2
        if inputList[mid] == key:
            return True
        elif inputList[mid] > key:
            top = mid - 1
        elif inputList[mid] < key:
            bottom = mid + 1

    return False

from math import ceil
import pdb

def main():
    input_list = [i for i in range(0, 99)]
    for i in input_list:
        value = binarySearch(input_list, i)
        print(i, value)


def binarySearch(input_list, key):
    if len(input_list) >= 1 :
        mid = ceil((len(input_list) - 1) / 2)

        # pdb.set_trace()
        if input_list[mid] == key:
            return True
        elif input_list[mid] > key:
            return binarySearch(input_list[:mid - 1], key)
        elif input_list[mid] < key:
            return binarySearch(input_list[mid + 1:], key)

    else:
        return False
main()

import random
def main():
    input_list = [random.randint(0, 99) for i in range(0, 99)]

    value = in_list(input_list, 34)
    print(value)



def in_list(input_list, key):
    index = (len(input_list) - 1 ) // 2
    mid = input_list[index]
    if len(input_list) == 1:
        return False
    elif mid == key:
        return True
    elif mid > key:
        return in_list(input_list[:index], key)
    elif mid < key:
        return in_list(input_list[index:], key)

main()

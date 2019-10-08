def main():
    list1 = [1, 2, 3, 4, 5, 6]

    print(list1)
    change(list1)
    print(list1)


def change(input_list):
    input_list.pop(len(input_list) // 2)

    
main()

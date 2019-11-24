def main():
    done = False
    num_list = []

    while not done:
        user_input = input("Please enter a number: ")

        if user_input == "":
            display_values(num_list)
            done = True
        else:
            try:
                num_list.append(float(user_input))
            except ValueError:
                print("What you entered wasn't a number, please try again")

def display_values(input_list):
    if len(input_list) == 0:
        print("The list is empty")
    else:
        print(input_list)
        print("You entered {} numbers".format(len(input_list)))
        print("Maximum value is : {}".format(max_linear_search(input_list)))
        print("Minumum value is : {}".format(min(input_list)))
        print("Sum of values is : {}".format(sum_values(input_list)))
        print("Average value is : {}".format(sum(input_list) / len(input_list)))


# While not nessecary, these functions make the above code a bit nicer
def max_linear_search(input_list):
    '''Finds the max value of an input_list, employes a linear search'''
    maximum = input_list[0]
    for num in input_list:
        if num > maximum:
            maximum = num
    return maximum

def sum_values(input_list):
    '''Calculates the maximum value of an input list'''
    total = 0
    for num in input_list:
        total += num
    return total

main()
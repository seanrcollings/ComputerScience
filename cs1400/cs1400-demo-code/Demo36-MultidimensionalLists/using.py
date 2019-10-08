import random


def main():
    list_1 = []
    for i in range(10):
        list_1.append([])
        for j in range(10):
            list_1[i].append(random.randint(0, 10))
    print(list_1)
    print("The sum of all: " + str(sum_all(list_1)))

    max_row, max_sum = max_row_sum(list_1)
    print("Row " + str(max_row) + " has the max sum of " + str(max_sum))

    max_col, max_sum = max_col_sum(list_1)
    print("Column " + str(max_col) + " has the max sum of " + str(max_sum))


def sum_all(lst):
    sum = 0

    for row in lst:
        for num in row:
            sum += num

    return sum

def max_row_sum(lst):
    curr_max_row = -1
    curr_max_sum = -1
    for i in range(len(lst)):
        row_sum = 0
        for j in range(len(lst[i])):
            row_sum += lst[i][j]

        if row_sum > curr_max_sum:
            curr_max_sum = row_sum
            curr_max_row = i

    return curr_max_row, curr_max_sum


def max_col_sum(lst):
    curr_max_col = -1
    curr_max_sum = -1
    for j in range(len(lst[0])):
        col_sum = 0
        for i in range(len(lst)):
            col_sum += lst[i][j]

        if col_sum > curr_max_sum:
            curr_max_sum = col_sum
            curr_max_col = j

    return curr_max_col, curr_max_sum

main()
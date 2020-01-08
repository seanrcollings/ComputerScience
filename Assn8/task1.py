'''
Sean Collings
CS1400-2
Assignment 8, Task 1
(Perfect number) A positive integer is called a perfect number if it is equal to the sum of all of its 
positive divisors, excluding itself. For example, 6 is the first perfect number, because 6 = 3 + 2 + 1. 
The next is 28 = 14 + 7 + 4 + 2 + 1. There are four perfect numbers less than 10,000. Write a program to find
these four numbers.

1 - Requirments specifications
    Find all the perfect numbers between 1 and 10000
    count up the iterations required to find them
    display both of those to the user

2 - System Analysis
    perfect_number = summation of all positive divisors

3 - System Design
    1 - Iterate through each number (i) between 1 and a 10000 
    2 - Iterate between each number (j) between 1 and i / 2
    3 - Check if i is divisible by j, if it is, add it to the divisor sum
    4 - Check if the divisor sum is equal to the i, if it is, add it to the perfect numbers array
    5 - Display the perfect number and the number of iterations

5 - Testing:
Output: 
[6, 28, 496, 8128]
Iterations of nested loop: x (could be below 48,500,000; 24,900,000; 16,000,000)
passed
'''
import math
import pdb
def find_perfect_numbers(num_range):
    '''Calls find_divisors for a number in a given range, then checks to see if the number is a perfect number'''
    perfect_numbers = []
    total_iterations = 0
    for num in num_range:

        divisors, iterations = find_divisors(num)
        total_iterations += iterations

        if sum(divisors) == num:
            perfect_numbers.append(num)
    
    print(perfect_numbers)
    print("Iterations of nested loop: %s" %(total_iterations))

def find_divisors(num):
    '''Finds all the divisors of a given number, emoloys sqrt to speed up the process significantly'''
    divisors = []
    i = 1

    while i <= math.sqrt(num):
        if num % i == 0 and num != i: # checks that the number is divisible by i and that i is not the number
            divisors.append(i)
            if num / i != num and num / i != i: # Essentially makes sure that there aren't any repeat factors or ones included
                divisors.append(int(num / i)) 
        i += 1

    return(divisors, i - 1)

find_perfect_numbers(range(1, 10000))

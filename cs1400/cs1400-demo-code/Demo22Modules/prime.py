def isPrime(num):
    divisor = 2
    while divisor <= num / 2:
        if num % divisor == 0:
                return False
        divisor += 1

    return True


def printPrimes(num_to_print):
    NUM_PER_LINE = 10
    count = 0
    number = 2

    while count < num_to_print:
        if isPrime(number):
            count += 1

            print(number, end=" ")
            if count % NUM_PER_LINE == 0:
                print()

        number += 1
        
def increment(val):
    print("original val: " + str(val))
    print("\tid: " + str(id(val)))
    val += 1
    print("new val: " + str(val))
    print("\tid: " + str(id(val)))


def main():
    num = 5
    print("before: " + str(num))
    print("\tid: " + str(id(num)))
    increment(num)
    print("after: " + str(num))
    print("\tid: " + str(id(num)))


main()
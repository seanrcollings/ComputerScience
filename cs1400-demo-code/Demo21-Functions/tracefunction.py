def maxVal(val1, val2):
    print("max_val() was called")
    if val1 < val2:
        print("maxVal() about to return")
        return val2
    else:
        print("maxVal() about to return")
        return val1


def main():
    print("main() was called")
    i = 5
    j = 10
    print("About to call maxVal()")
    k = maxVal(i, j)
    print("maxVal() has returned")
    print("The max value is: " + str(k))


print("Calling main()")
main()
print("main() is finished")

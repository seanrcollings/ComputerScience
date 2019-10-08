def main():
    print("Concatenation (+): ", end="")
    print("First String" + "Second String")
    print()

    print("Repetition (*): ", end="")
    print("One String" * 6)
    print()

    print("Index ([index]): ", end="")
    str1 = "This is a string"
    print(str1[12])
    print()

    print("Slice ([start:end]): ", end="")
    str2 = "Slice this string"
    print(str2[3:12])
    print()

    print("in: ", end="")
    str3 = "Look in this string"
    print("ook" in str3, end=" ")
    print("zzz" in str3)
    print()


main()
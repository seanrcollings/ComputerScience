print(format("Multiplication Table", "^40s"))
print()
print("   ", end="")

for i in range(1, 10):
    print(format(i, ">4"), end="")
print()

for i in range(40):
    print('-', end="")
print()

for i in range(1, 10):
    print(i, "|", end="")
    for j in range(1, 10):
        print(format(i * j, "4d"), end="")
    print()
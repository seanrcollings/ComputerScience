# By list element
list1 = [4, 2, 1, "Dog", "Cat", "Elephant"]

for e in list1:
    print(e)

print()
# By index number
for i in range(len(list1)):
    print(list1[i])

print()
list2 = [3, 2, 54, 1, 32, 76, 13]
for i in range(len(list2) - 1):
    print(list2[i] + list2[i + 1])
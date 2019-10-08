list1 = [x for x in range(10)]
print(list1)

print()
list2 = [0.5 * x for x in list1]
print(list2)

print()
list3 = [x for x in list2 if x < 4]
print(list3)
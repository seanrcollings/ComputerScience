list1 = [3, 32, 54, 892, 24, 123]

list2 = list1 # This does not copy
print("=: ", id(list1), id(list2))

list3 = [x for x in list1]
print("Comprehension: ", id(list1), id(list3))

list4 = [] + list1
print("Shortcut: ", id(list1), id(list4))
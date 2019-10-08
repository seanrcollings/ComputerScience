list1 = [1, 2, 3, 4, 3, 2, 1]
list2 = ["Apple", "Banana", "Cherry"]

print(list1)

list1.append("New!!!")
print(list1)

list1.extend(list2)
print(list1)

print(list1.index("New!!!"))

print(list1.insert(3, "Inserted"))

list1.reverse()
print(list1)

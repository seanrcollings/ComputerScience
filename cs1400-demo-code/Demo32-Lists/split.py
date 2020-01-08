str1 = "My name is John"
list1 = str1.split()
print(list1)

print()
str2 = "06/18/2018"
list2 = str2.split("/")
print(list2)

str3 = input("Enter numbers separated by a space: ")
nums = str3.split()
list3 = [eval(x) for x in nums]
print(sum(list3))
# is is the same as comparing id's

str1 = "Hello"
str2 = str1
str3 = "Goodbye"
str4 = "Hello" * 6
str5 = "Hello" * 6

print(str1 is str2, id(str1) == id(str2))
print(str1 is str3, id(str1) == id(str3))
print(str4 is str5, id(str4) == id(str5))


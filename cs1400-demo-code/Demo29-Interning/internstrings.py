
print("Repeat 4 Times")
str1 = "Hello" * 4
str2 = "Hello" * 4

print("   == :", str1 == str2)
print("id == :", id(str1) == id(str2))
print("   is :", str1 is str2)

print("\nNow Repeat 5 Times")
str1 = "Hello" * 5
str2 = "Hello" * 5

print("   == :", str1 == str2)
print("id == :", id(str1) == id(str2))
print("   is :", str1 is str2)

print("\nMake sure you're comparing what you want to")
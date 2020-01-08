
print("Create some int objects")
num1 = int('256')
num2 = int('256')

print("   == :", num1 == num2)
print("id == :", id(num1) == id(num2))
print("   is :", num1 is num2)

print("\nCreate some larger ones")
num1 = int('257')
num2 = int('257')

print("   == :", num1 == num2)
print("id == :", id(num1) == id(num2))
print("   is :", num1 is num2)

print("\nMake sure you're comparing what you want to")
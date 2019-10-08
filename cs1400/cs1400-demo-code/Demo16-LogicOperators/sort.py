num1, num2, num3 = eval(input("Enter three numbers: "))

if num1 > num2:
    num1, num2 = num2, num1
print(num1, num2, num3)

if num2 > num3:
    num2, num3 = num3, num2
print(num1, num2, num3)

if num1 > num2:
    num1, num2 = num2, num1
print(num1, num2, num3)

print("The sorted numbers are", num1, num2, num3)
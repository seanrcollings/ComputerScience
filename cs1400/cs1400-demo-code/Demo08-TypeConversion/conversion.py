value = 1
integer = 1
floating = 1.0
string = "2"

print(value + integer)
print(value + floating)
print(value + int(string)) # turn a string into an integer
print(value + float(string)) # turn a string into a floating point

# New way to print with +
print("I " + "can " + "use + symbols to " + "connect strings")
print("The " + "value is " + str(value)) # value has to be turned into a string


char1 = "m" # just a plain old character
char2 = "\u8f13" # unicode character in hexidecimal

print(char1)
print(char2)

# find the ordinal number
print(ord(char1))
print(ord(char2))

# print the character for the ordinal value
print(chr(109))
print(chr(36627))

# Escape sequences
print("\tThis is a tab")
print("This is a\nnew line")
print("This is a\n\tnew line with a tab")
print("This as \"a quote\"")
print("This uses a \\")
print("This uses a\rcarriage return")
print("This uses a backspace so you can correct erroes\b\brs" +
      " in the most awkward way possible")

print("Look, two prints", end = "")
print(" and they're on one line")


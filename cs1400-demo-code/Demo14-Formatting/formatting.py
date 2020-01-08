# Float
print(format(52.12312, "10.2f"))
print(format(52.12312, "<10.2f"))
print(format(42, "10b"))
# Scientific Notation
print(format(57.467123, "10.2e"))
# Percentage
print(format(0.12341, "10.2%"))
# Alignment
print(format(-523.1234, "=-10.2f"))
# Integers
print(format(342134, "10d"))
# Strings
print(format("this is a string", "^30s"), end="X")
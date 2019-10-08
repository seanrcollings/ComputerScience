# Let's do the same for PI so we don't make mistakes

# using the float() function you can convert a numeric string
# into a value. It will convert a whole number or decimal number
# into a float type
radius = float(input("Enter a number: ")) # Assign the variable 'radius' the value 8
PI = 3.14159

print("Circumference is", 2 * PI * radius)

# Now do the same for the Area
print("Area is", radius * radius * PI)